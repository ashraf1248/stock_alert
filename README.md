# Stock Price Alert System

This Python script is designed to fetch the latest stock price using the Alpha Vantage API and send an alert via Twilio SMS.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3.x installed
- Twilio account SID, authentication token, and Twilio phone numbers (sender and receiver)
- Alpha Vantage API key

## Installation

1. Install required libraries:

   ```bash
   pip install twilio alpha_vantage
   ```

2. **Set up your configuration:**

   Open the script file (`stock_alert.py`) and update the following information:

   ```python
   # Alpha Vantage API Key
   alpha_vantage_api_key = "your_alpha_vantage_api_key"

   # Twilio Configurations
   account_sid = 'your_twilio_account_sid'
   auth_token = 'your_twilio_auth_token'
   twilio_num = 'your_twilio_phone_number'  # Twilio phone number
   your_num = 'your_phone_number'  # Your phone number
   ```

## Usage

Run the script to get the latest stock price and receive an SMS alert:

```bash
python stock_alert.py
```

The script fetches the latest stock price for a predefined stock symbol (in this case, 'AAPL') using the Alpha Vantage API. If successful, it sends an SMS alert using the Twilio API.

## Customization

- **Change Stock Symbol:**
  Update the `stock_symbol` variable in the `main()` function to the desired stock symbol.

- **Customize Alert Message:**
  Modify the `message` variable in the `send_stock_alert` function to customize the alert message.

## Schedule for Daily Alerts

To receive daily alerts, consider scheduling the script to run automatically using a task scheduler (e.g., cron on Linux, Task Scheduler on Windows) or a cloud-based service like AWS Lambda.

Example cron job to run the script every day at 9 AM:

```bash
0 9 * * * /path/to/python /path/to/stock_alert.py
```


Feel free to adapt and customize this template based on your preferences and additional details about your project.
