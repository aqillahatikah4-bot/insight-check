from flask import Flask, send_from_directory, Response
from flask_cors import CORS
import requests
import os

app = Flask(__name__, static_folder='.')
CORS(app)

# ?? Route untuk paparkan laman utama (index.html)
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# ?? Route untuk favicon (supaya tiada error 404)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.', 'favicon.ico')

# ?? Route untuk ambil data CSV dari Google Sheets
@app.route('/sheet-csv')
def sheet_csv():
    try:
        sheet_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRJgCHqA6X4rpAiBTAL7tvZicdP4gBiVGHCPIkLyz9ZApil4xHHQC40-BltSS2QR8TllRn9thY0Hw1D/pub?gid=1751401824&single=true&output=csv"
        response = requests.get(sheet_url)
        response.raise_for_status()  # kalau ada error, terus raise
        return Response(response.text, mimetype='text/csv')
    except Exception as e:
        return {"error": str(e)}, 500

# ?? Jalankan app di Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

