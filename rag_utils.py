import re
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ✅ Load API key securely
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# ✅ Use Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def scrape_screener_data(company):
    url = f"https://www.screener.in/company/{company.upper()}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": f"Could not fetch data for {company}"}

    soup = BeautifulSoup(response.text, "html.parser")
    data = {}

    try:
        ratios = soup.find("div", class_="company-ratios")
        rows = ratios.find_all("li")

        for row in rows:
            key_tag = row.find("span", class_="name")
            val_tag = row.find("span", class_="value")
            if key_tag and val_tag:
                data[key_tag.text.strip()] = val_tag.text.strip()
    except:
        data["error"] = "Could not parse company data"

    return data

def ask_query(query: str):
    match = re.search(r'of\s+([A-Z.]+)', query.upper())
    company = match.group(1) if match else "RELIANCE"

    data = scrape_screener_data(company)
    if "error" in data:
        return f"⚠️ {data['error']}"

    context = "\n".join([f"{k}: {v}" for k, v in data.items()])
    response = model.generate_content(
        f"Use the following context to answer the query:\n\n{context}\n\nQuery: {query}"
    )

    return response.text
