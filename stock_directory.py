import requests
from bs4 import BeautifulSoup
import json
import os
import time

# 🛡️ Load existing directory safely
json_path = "stock_directory.json"
if os.path.exists(json_path) and os.path.getsize(json_path) > 0:
    with open(json_path, "r", encoding="utf-8") as f:
        try:
            company_directory = json.load(f)
        except json.JSONDecodeError:
            print("⚠️ JSON file is invalid. Starting with an empty directory.")
            company_directory = []
else:
    company_directory = []

# Create set of company IDs that have already been added
existing_ids = {entry["cmpy_id"] for entry in company_directory}

# 🌐 Start from any valid stockData page to get company links
directory_url = "https://edge.pse.com.ph/companyPage/stockData.do?cmpy_id=643&security_id=586"
base_url = "https://edge.pse.com.ph"

response = requests.get(directory_url)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.select("a[href*='companyInformation/form.do?cmpy_id=']")

# 🔁 Loop through found company links
for link in links:
    name = link.get_text(strip=True)
    href = link.get("href")
    cmpy_id = href.split("cmpy_id=")[-1]

    # Skip if already scraped
    if cmpy_id in existing_ids:
        continue

    stock_url = f"{base_url}/companyPage/stockData.do?cmpy_id={cmpy_id}"
    stock_response = requests.get(stock_url)
    if stock_response.status_code != 200:
        print(f"⚠️ Failed to fetch stock page for cmpy_id={cmpy_id}")
        continue

    stock_soup = BeautifulSoup(stock_response.text, "html.parser")

    # 🔍 Extract security_id and stock_symbol
    select_tag = stock_soup.find("select", {"name": "security_id"})
    option_tag = select_tag.find("option") if select_tag else None
    security_id = option_tag.get("value") if option_tag else None
    stock_symbol = option_tag.get_text(strip=True) if option_tag else None

    # 🏢 Extract company name from div.compInfo
    comp_info = stock_soup.find("div", {"class": "compInfo"})
    company_name = comp_info.get_text(strip=True) if comp_info else name

    # 📊 Extract status from second table
    status = "Unknown"
    tables = stock_soup.find_all("table", class_="view")
    stock_table = tables[1] if len(tables) > 1 else None

    if stock_table:
        for row in stock_table.find_all("tr"):
            cells = row.find_all(["th", "td"])
            for i in range(0, len(cells) - 1, 2):
                label = cells[i].get_text(strip=True)
                value = cells[i + 1].get_text(strip=True)
                if label == "Status":
                    status = value
                    break

    # 📦 Assemble and record the entry
    entry = {
        "company_name": company_name,
        "stock_symbol": stock_symbol,
        "cmpy_id": cmpy_id,
        "security_id": security_id,
    }

    company_directory.append(entry)
    print(f"✓ Added: {name} → cmpy_id: {cmpy_id}, security_id: {security_id}, status: {status}")
    time.sleep(0.5)

# 💾 Save final JSON
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(company_directory, f, indent=2, ensure_ascii=False)

print(f"\n📦 Directory updated! Total companies: {len(company_directory)}")