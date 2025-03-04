import requests
import re

PACKAGE_NAME = "tidyflow"  
README_FILE = "README.md"

def get_total_downloads(package):
    url = f"https://pypistats.org/api/packages/{package}/overall"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return sum(item["downloads"] for item in data["data"])
    return None

def update_readme(downloads):
    with open(README_FILE, "r") as file:
        content = file.read()

    new_badge = f"https://img.shields.io/badge/{PACKAGE_NAME}-{downloads}-blue"
    updated_content = re.sub(r"https://img.shields.io/badge/.*?-blue", new_badge, content)

    with open(README_FILE, "w") as file:
        file.write(updated_content)

downloads = get_total_downloads(PACKAGE_NAME)
if downloads:
    update_readme(downloads)
    print(f"Updated README with {downloads} total downloads.")
else:
    print("Failed to fetch download data.")
