from flask import Flask, request, jsonify
import time  # to simulate delay

app = Flask(__name__)

@app.route('/api/honeypot', methods=['POST'])
def honeypot_scan():
    data = request.get_json()  # ✅ FIXED FROM request.form
    contract = data.get('contract')
    chain = data.get('chain')

    if not contract or not chain:
        return jsonify({'error': 'Missing contract address or chain'}), 400

    # simulate scanning process
    print(f"🔍 Scanning {contract} on {chain}...")
    time.sleep(2)

    # simulated result
    result = {
        "contract": contract,
        "chain": chain,
        "honeypot": False,
        "buy_tax": 5,
        "sell_tax": 5,
        "notes": "No honeypot detected"
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
