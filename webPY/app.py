# flask_web/app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

html = """ 
<br> API TESTING 
<br> POST: 
<br>
<form method='POST' action='/'>
    <input type='text' name='postmsg'>
    <input type='submit'>
</form>
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        app.logger.info(request.form.get("postmsg"))
    return html


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)

