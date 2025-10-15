from flask import Flask, Response
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # benarkan permintaan dari semua domain

# Gantikan dengan link Google Sheets kamu
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRJgCHqA6X4rpAiBTAL7tvZicdP4gBiVGHCPIkLyz9ZApil4xHHQC40-BltSS2QR8TllRn9thY0Hw1D/pub?gid=1751401824&single=true&output=csv"

@app.route("/sheet-csv")
def get_sheet_csv():
    try:
        r = requests.get(SHEET_URL, timeout=10)
        return Response(r.content, mimetype="text/csv")
    except Exception as e:
        return Response(f"Error fetching sheet: {e}", status=500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
