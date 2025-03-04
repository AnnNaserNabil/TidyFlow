import requests
import re

PACKAGE_NAME = "tidyflow"  

# Fetch the overall download count from PyPIStats
url = f"https://pypistats.org/api/packages/{PACKAGE_NAME}/overall"
response = requests.get(url)
data = response.json()

# Sum up all downloads
total_downloads = sum(item["downloads"] for item in data["data"])

# Read the README file
with open("README.md", "r") as file:
    readme_content = file.read()

# Replace old badge with the updated value
new_badge = f"![PyPI - Downloads](https://img.shields.io/badge/Downloads-{total_downloads}-blue)"
updated_content = re.sub(r"!\[PyPI - Downloads\]\(.*?\)", new_badge, readme_content)

# Write back to README.md
with open("README.md", "w") as file:
    file.write(updated_content)

print(f"Updated README with {total_downloads} downloads!")
