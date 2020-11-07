# flask_web/app.py

from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

