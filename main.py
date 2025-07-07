from fastapi import FastAPI
from signals import scan_and_send_signals

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Rage Sniper Bot is running"}

@app.post("/signals")
def trigger_signals():
    scan_and_send_signals()
    return {"message": "Signals triggered"}
