from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/signals', methods=['POST'])
def signals():
    data = request.json
    print("Signal received:", data)
    return {'status': 'received'}, 200

@app.route('/', methods=['GET'])
def home():
    return "Rage Sniper Bot is running", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)