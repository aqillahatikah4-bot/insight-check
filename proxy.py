from flask import Flask, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRJgCHqA6X4rpAiBTAL7tvZicdP4gBiVGHCPIkLyz9ZApil4xHHQC40-BltSS2QR8TllRn9thY0Hw1D/pub?gid=1751401824&single=true&output=csv"

@app.route("/sheet-csv")
def sheet_csv():
    try:
        res = requests.get(SHEET_URL)
        res.raise_for_status()
        return Response(res.text, content_type="text/csv")
    except Exception as e:
        return Response(f"Error: {e}", status=500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
