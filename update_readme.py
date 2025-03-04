import requests
import re

PACKAGE_NAME = "tidyflow"
README_FILE = "README.md"
API_URL = f"https://pypistats.org/api/packages/{PACKAGE_NAME}/overall"

def fetch_all_time_downloads():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()["data"]
        return sum(item["downloads"] for item in data)
    return None

downloads = fetch_all_time_downloads()
if downloads is not None:
    with open(README_FILE, "r") as file:
        content = file.read()

    badge_pattern = rf"!\[PyPI - Downloads\]\(https://img.shields.io/badge/{PACKAGE_NAME}.*?\)"
    new_badge = f"![PyPI - Downloads](https://img.shields.io/badge/{PACKAGE_NAME}-{downloads}-blue)"
    updated_content = re.sub(badge_pattern, new_badge, content)

    with open(README_FILE, "w") as file:
        file.write(updated_content)

    print(f"Updated README for {PACKAGE_NAME} with {downloads} downloads!")
