from flask import Flask, Response, send_from_directory
import requests, os

app = Flask(__name__, static_folder='.')

SHEET_URL = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vRJgCHqA6X4rpAiBTAL7tvZicdP4gBiVGHCPIkLyz9ZApil4xHHQC40-"
             "BltSS2QR8TllRn9thY0Hw1D/pub?gid=1751401824&single=true&output=csv")

@app.route('/')
def home():
    # Jika mahu terus paparkan index.html dari server
    return send_from_directory('.', 'index.html')

@app.route('/sheet-csv')
def sheet_csv():
    try:
        res = requests.get(SHEET_URL)
        res.raise_for_status()
        return Response(res.text, content_type="text/csv")
    except Exception as e:
        return Response(f"Error: {str(e)}", status=500)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

