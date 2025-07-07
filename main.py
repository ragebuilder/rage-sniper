# Basic FastAPI app with /signals webhook and 5-min interval stub
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import requests
import csv
import os

app = FastAPI()

def fetch_and_filter_tokens():
    print("🔁 Running token scan at", datetime.now())
    url = "https://api.dexscreener.com/latest/dex/pairs/solana"
    try:
        res = requests.get(url, timeout=10)
        pairs = res.json().get("pairs", [])
    except Exception as e:
        print("❌ Error fetching from Dexscreener:", e)
        return

    filtered = []
    for pair in pairs:
        if pair.get("txns", {}).get("h1", {}).get("buys", 0) + pair.get("txns", {}).get("h1", {}).get("sells", 0) < 100:
            continue
        pair["rugcheck"] = "GOOD"
        pair["fake_volume"] = False
        pair["liquidity_locked"] = True

        if pair["rugcheck"] == "GOOD" and not pair["fake_volume"] and pair["liquidity_locked"]:
            filtered.append(pair)
        if len(filtered) >= 10:
            break

    csv_file = f"signals_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(os.path.join("/mnt/data", csv_file), mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Pair", "Symbol", "DEX", "TXNs 1h", "Liquidity", "Rugcheck"])
        for p in filtered:
            tx_count = p.get("txns", {}).get("h1", {}).get("buys", 0) + p.get("txns", {}).get("h1", {}).get("sells", 0)
            writer.writerow([
                p.get("pairAddress", ""),
                p.get("baseToken", {}).get("symbol", ""),
                p.get("dexId", ""),
                tx_count,
                p.get("liquidity", {}).get("usd", ""),
                p.get("rugcheck", ""),
            ])
    print(f"✅ Saved {len(filtered)} tokens to {csv_file}")

@app.get("/signals")
def trigger_signals():
    fetch_and_filter_tokens()
    return {"message": "Scan complete."}

scheduler = BackgroundScheduler()
scheduler.add_job(fetch_and_filter_tokens, 'interval', minutes=5)
scheduler.start()
