from flask import Flask, Response
import requests

app = Flask(__name__)

# ?? URL CSV dari Google Sheets kamu
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRJgCHqA6X4rpAiBTAL7tvZicdP4gBiVGHCPIkLyz9ZApil4xHHQC40-BltSS2QR8TllRn9thY0Hw1D/pub?gid=1751401824&single=true&output=csv"

@app.route('/')
def home():
    return "<h2>? Proxy Server Berjaya Jalan!</h2><p>Gunakan endpoint <b>/sheet-csv</b> untuk akses data Google Sheets.</p>"

@app.route('/sheet-csv')
def sheet_csv():
    try:
        # Fetch CSV dari Google Sheets
        res = requests.get(SHEET_URL)
        res.raise_for_status()

        # Hantar balik CSV ke frontend
        response = Response(res.text, content_type="text/csv; charset=utf-8")
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    except Exception as e:
        print("? Ralat:", e)
        return Response("Gagal ambil data CSV.", status=500)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

