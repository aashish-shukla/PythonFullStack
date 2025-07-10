import requests

TIINGO_API_KEY = "dfa7eb9f0661a6c31e04bb661e18c8b7f55926d7"

def get_tiingo_price(ticker):
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {TIINGO_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['close']
    return None

def get_tiingo_profile(ticker):
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {TIINGO_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return {}

def search_tiingo(query):
    url = f"https://api.tiingo.com/tiingo/utilities/search?query={query}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {TIINGO_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []