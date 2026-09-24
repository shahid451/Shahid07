import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_contributions(username="Shahid07"):
    url = f"https://github.com/users/{username}/contributions"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching data: Status code {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    tooltips = soup.find_all("tool-tip")
    
    contributions = []
    for tip in tooltips:
        for_id = tip.get("for", "")
        rect = soup.find("td", id=for_id) or soup.find("rect", id=for_id)
        if rect:
            count_text = tip.text.strip()
            date = rect.get("data-date", "")
            level = rect.get("data-level", "0")
            contributions.append({
                "date": date,
                "count": count_text,
                "level": level
            })

    os.makedirs("data", exist_ok=True)
    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(contributions, f, indent=2)
        
    print(f"Contributions saved to data/contributions.json ({len(contributions)} days found)")

if __name__ == "__main__":
    fetch_contributions()
