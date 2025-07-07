from flask import Flask, request
from utils import evaluate_tokens
import csv
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Rage Sniper Bot is running"

@app.route("/signals", methods=["POST", "GET"])
def signals():
    tokens = evaluate_tokens()
    output = []
    for token in tokens:
        output.append({
            "name": token['name'],
            "address": token['address'],
            "volume": token['volume'],
            "tx_1h": token['tx_1h'],
            "rugcheck": token['rugcheck_status'],
            "fake_volume": token['fake_volume'],
            "liquidity_locked": token['liquidity_locked'],
            "influencer_score": token.get('influencer_score', 'pending')
        })
    with open("/mnt/data/signal_results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=output[0].keys())
        writer.writeheader()
        writer.writerows(output)
    return {"tokens": output}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
