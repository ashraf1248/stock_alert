import os
from twilio.rest import Client
from alpha_vantage.timeseries import TimeSeries
def get_latest_stock_price(stock_symbol):
  alpha_vantage_api_key = "Key"
  alpha_vantage = TimeSeries(alpha_vantage_api_key)
  try:
    data,_ = alpha_vantage.get_quote_endpoint(symbol=stock_symbol)
    latest_price = float(data['05. price'])
    return latest_price
  except Exception as e:
    print(f"Error: {e}")

def send_stock_alert(symbol,price):
  account_sid = 'ID'
  auth_token = 'TOKEN'
  twilio_num = 'NUM'
  your_num = 'NUM'
  client = Client(account_sid, auth_token)
  message = f"Stock price of {symbol} is now {price}. Time to buy or sell."
  print(f"Stock price of {symbol} is now {price}. Time to buy or sell.")
  client.messages.create(
    body = message,
    from_=twilio_num,
    to=your_num
  )

def main():
  stock_symbol = 'AAPL'
  latest_price = get_latest_stock_price(stock_symbol)
  send_stock_alert(stock_symbol, latest_price)

main()
