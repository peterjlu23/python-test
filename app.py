from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_spy_data():
    # Polygon API URL for SPY's details on a specific date
    url = "https://api.polygon.io/v1/open-close/SPY/2024-07-17?adjusted=true&apiKey=vAFV5Hzy2OrTozBZuOFw5EwpZdNQ1leZ"

    # Sending HTTP GET request to Polygon API
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Parse JSON data
        
        # Extract and format the desired stock data
        symbol = data['symbol']
        open_price = data['open']
        high_price = data['high']
        low_price = data['low']
        close_price = data['close']
        
        # Build a string to display the data
        result = f"""<h1>Stock Data for {symbol}</h1>
                     <p>Open: {open_price}</p>
                     <p>High: {high_price}</p>
                     <p>Low: {low_price}</p>
                     <p>Close: {close_price}</p>"""
        return result
    else:
        return "Failed to fetch data from Polygon API"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

