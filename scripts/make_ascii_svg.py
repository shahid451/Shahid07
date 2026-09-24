import os
import glob
from PIL import Image

def image_to_ascii_svg(width=100):
    # Search for any prepped png or image in current directory
    png_files = glob.glob("source-prepped*.png") + glob.glob("*.png")
    if not png_files:
        print("Error: Koi .png image file nahi mili!")
        return

    img_path = png_files[0]
    print(f"Using image file: {img_path}")

    img = Image.open(img_path).convert("L")
    RAMP = " .`:-=+*cs#%@"
    
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
        '  text {{ font-family: monospace; font-size: 10px; fill: #8b949e; white-space: pre; }}',
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
    
    with open("avi-ascii.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))
        
    print(f"ASCII SVG generated successfully: avi-ascii.svg")

if __name__ == "__main__":
    image_to_ascii_svg()
