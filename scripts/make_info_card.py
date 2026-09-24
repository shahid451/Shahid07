import os

def create_info_card(output_svg="info-card.svg"):
    # Personal info details - Aap isko apne acche se customize kar sakte hain
    username = "Shahid Pathan"
    role = "Computer Science Student / Software Engineer"
    stack = "Java, Python, JavaScript, Git, GitHub"
    highlights = "Backend Dev, Competitive Programming, AI Tools"
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 490 350" width="490" height="350">
  <style>
    .bg {{ fill: #0d1117; rx: 6px; }}
    .title {{ font-family: monospace; font-size: 14px; font-weight: bold; fill: #58a6ff; }}
    .label {{ font-family: monospace; font-size: 12px; font-weight: bold; fill: #79c0ff; }}
    .value {{ font-family: monospace; font-size: 12px; fill: #c9d1d9; }}
    .line {{ stroke: #30363d; stroke-width: 1; }}
    
    .fade-in {{
      opacity: 0;
      animation: fadeIn 0.5s ease-in-out forwards;
    }}
    
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(5px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
  </style>
  
  <rect width="100%" height="100%" class="bg" />
  
  <!-- Header Bar -->
  <text x="20" y="35" class="title fade-in" style="animation-delay: 0.1s;">{username}@github ~ $ neofetch</text>
  <line x1="20" y1="50" x2="470" y2="50" class="line" />
  
  <!-- Info Rows -->
  <g class="fade-in" style="animation-delay: 0.3s;">
    <text x="20" y="85" class="label">OS:</text>
    <text x="110" y="85" class="value">GitHub Profile OS / Linux</text>
  </g>
  
  <g class="fade-in" style="animation-delay: 0.5s;">
    <text x="20" y="120" class="label">Role:</text>
    <text x="110" y="120" class="value">{role}</text>
  </g>
  
  <g class="fade-in" style="animation-delay: 0.7s;">
    <text x="20" y="155" class="label">Tech Stack:</text>
    <text x="110" y="155" class="value">{stack}</text>
  </g>
  
  <g class="fade-in" style="animation-delay: 0.9s;">
    <text x="20" y="190" class="label">Highlights:</text>
    <text x="110" y="190" class="value">{highlights}</text>
  </g>
  
  <line x1="20" y1="220" x2="470" y2="220" class="line" />
  
  <!-- Color Palette block (Neofetch style) -->
  <g class="fade-in" style="animation-delay: 1.1s;">
    <rect x="20" y="240" width="20" height="20" fill="#ff7b72" rx="3" />
    <rect x="50" y="240" width="20" height="20" fill="#ffa657" rx="3" />
    <rect x="80" y="240" width="20" height="20" fill="#d2a8ff" rx="3" />
    <rect x="110" y="240" width="20" height="20" fill="#79c0ff" rx="3" />
    <rect x="140" y="240" width="20" height="20" fill="#7ee787" rx="3" />
  </g>
</svg>'''

    with open(output_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    print(f"Info Card SVG generated: {output_svg}")

if __name__ == "__main__":
    create_info_card()
