<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

# 🌦 Simple Weather Scraper

A lightweight Python script to fetch current weather information for any city using the terminal-friendly [wttr.in](https://wttr.in) service.

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

## 📌 Features

- Get concise weather info for any city.
- Uses `requests` and `BeautifulSoup` (though not required for current usage).
- Clean and beginner-friendly code.
- Error handling included.

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

## 🚀 Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/simple-weather-scraper.git
cd simple-weather-scraper
````

### 2. Install dependencies

```bash
pip install requests beautifulsoup4
```

### 3. Run the script

```bash
python weather_scraper.py
```

### Example Output

```
Lahore: 🌤 +39°C
```
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

## 🧠 Code Overview

```python
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
```
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

> 💡 Note: The script currently uses a simple text-based output. You can modify it to fetch detailed reports or parse other formats supported by wttr.in.

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">
