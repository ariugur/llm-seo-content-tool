import requests
import os
from dotenv import load_dotenv
from langchain.tools import Tool

load_dotenv()  # .env dosyasını yükle

SEOGPT_URL = "https://seogpt.dev:8010/generate"
API_KEY = os.getenv("MASTER_KEY")  # .env içinden çek

def seo_generate_tool(prompt: str, persona: str = "algo-chill") -> str:
    payload = {
        "prompt": prompt,
        "persona": persona
    }
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }

    response = requests.post(SEOGPT_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("content_html", "[⛔ İçerik döndürülemedi.]")
    else:
        return f"[❌ Hata]: {response.status_code} - {response.text}"

seo_tool = Tool(
    name="SEOContentGenerator",
    description="SEO uyumlu HTML içerik oluşturur. prompt ve persona alır.",
    func=seo_generate_tool
)
