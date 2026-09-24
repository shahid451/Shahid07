import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep(input_path, output_path="source-prepped.png"):
    inp = Image.open(input_path)
    out = remove(inp)
    
    img_np = np.array(out)
    if img_np.shape[2] == 4:
        alpha = img_np[:, :, 3]
        rgb = img_np[:, :, :3]
        gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
        
        white_bg = np.ones_like(gray) * 255
        alpha_factor = alpha / 255.0
        gray = (gray * alpha_factor + white_bg * (1 - alpha_factor)).astype(np.uint8)
    else:
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    cv2.imwrite(output_path, enhanced)
    print(f"Prepped image saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prep(sys.argv[1])
    else:
        print("Usage: python scripts/prep_photo.py <path_to_photo>")
from PIL import Image

def image_to_ascii_svg(img_path="source-prepped.png", output_svg="avi-ascii.svg", width=100):
    RAMP = " .`:-=+*cs#%@"
    img = Image.open(img_path).convert("L")
    
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.55)
    img = img.resize((width, height))
    
    pixels = img.getdata()
    lines = []
    
    for y in range(height):
        line_chars = ""
        for x in range(width):
            pixel_val = pixels[y * width + x]
            ramp_idx = int((pixel_val / 255) * (len(RAMP) - 1))
            line_chars += RAMP[ramp_idx]
        lines.append(line_chars)

    svg_width = width * 7
    svg_height = height * 12
    
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">',
        '<style>',
        '  text { font-family: monospace; font-size: 10px; fill: #8b949e; white-space: pre; }',
        '</style>',
        f'<rect width="100%" height="100%" fill="#0d1117"/>'
    ]
    
    delay = 0.03
    for idx, line in enumerate(lines):
        y_pos = (idx + 1) * 12
        escaped_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        
        svg_lines.append(
            f'<text x="10" y="{y_pos}">'
            f'<animate attributeName="opacity" from="0" to="1" begin="{idx * delay}s" dur="0.1s" fill="freeze" />'
            f'{escaped_line}</text>'
        )
        
    svg_lines.append('</svg>')
    
    with open(output_svg, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
        
    print(f"ASCII SVG generated: {output_svg}")

if __name__ == "__main__":
    image_to_ascii_svg()