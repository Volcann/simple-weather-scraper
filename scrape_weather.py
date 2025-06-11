import requests
from bs4 import BeautifulSoup

def scrape_weather_detailed(city):
    url = f"https://wttr.in/{city}?format=3"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return {"error": f"Failed to fetch data. Status: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

print(scrape_weather_detailed("Lahore"))
