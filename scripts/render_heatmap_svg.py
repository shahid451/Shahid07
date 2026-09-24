import json
import os

def render_svg():
    json_path = "data/contributions.json"
    if not os.path.exists(json_path):
        print("Error: data/contributions.json nahi mila. Pehle fetch script chalayein!")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # GitHub contribution colors
    colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
    
    box_size = 10
    gap = 3
    start_x = 20
    start_y = 30

    svg_width = 860
    svg_height = 140

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}" width="{svg_width}" height="{svg_height}">',
        '<style>',
        '  .bg { fill: #0d1117; rx: 6px; }',
        '  text { font-family: monospace; font-size: 12px; fill: #8b949e; }',
        '  rect.day { rx: 2px; opacity: 0; animation: fadeIn 0.4s ease-in-out forwards; }',
        '  @keyframes fadeIn { to { opacity: 1; } }',
        '</style>',
        f'<rect width="100%" height="100%" class="bg"/>',
        f'<text x="20" y="20">GitHub Contributions (Past Year)</text>'
    ]

    col = 0
    row = 0
    for idx, item in enumerate(data):
        level = int(item.get("level", 0))
        color = colors[level] if level < len(colors) else colors[-1]
        
        x = start_x + col * (box_size + gap)
        y = start_y + row * (box_size + gap)
        
        delay = (col * 0.02) + (row * 0.01)
        
        svg_lines.append(
            f'<rect class="day" x="{x}" y="{y}" width="{box_size}" height="{box_size}" fill="{color}" style="animation-delay: {delay:.2f}s;"/>'
        )
        
        row += 1
        if row >= 7:
            row = 0
            col += 1

    svg_lines.append('</svg>')

    with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(svg_lines))

    print("Heatmap SVG generated successfully: contrib-heatmap.svg")

if __name__ == "__main__":
    render_svg()
