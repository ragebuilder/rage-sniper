import requests
import csv
from datetime import datetime

def is_rugcheck_good(token_address):
    url = f"https://api.rugcheck.xyz/api/token/{token_address}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        return data.get("status") == "success" and data.get("data", {}).get("audit") == "GOOD"
    except:
        return False

def scan_and_send_signals():
    # Sample dummy data (replace with real Dexscreener API integration)
    token_data = [
        {"token": "Token1", "address": "addr1", "1h_tx": 120, "rugcheck": True, "liquidity": "locked"},
        {"token": "Token2", "address": "addr2", "1h_tx": 95, "rugcheck": False, "liquidity": "unlocked"},
    ]

    results = []
    for token in token_data:
        if token["1h_tx"] >= 100 and token["rugcheck"] and token["liquidity"] == "locked":
            results.append(token)

    filename = f"/mnt/data/signals_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["token", "address", "1h_tx", "rugcheck", "liquidity"])
        writer.writeheader()
        writer.writerows(results)

    print(f"Saved {len(results)} tokens to {filename}")
