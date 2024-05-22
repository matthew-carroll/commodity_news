import os
import requests

def get_current_gold_price_from_metalpricesapi():
  api_key = os.environ["METALPRICE_API_KEY"]
  url = "https://api.metalpriceapi.com/v1/latest?api_key=" + api_key + "&base=USD&currencies=XAU"

  response = requests.get(url)
  data = response.json()

  # Example Response
  # {
  #   'success': True, 
  #   'base': 'USD', 
  #   'timestamp': 1716335999, 
  #   'rates': {
  #     'XAU': 0.0004130872
  #    }
  # }

  return {
    "timestamp": data["timestamp"],
    "price": 1.0 / data["rates"]["XAU"]
  }

def get_current_gold_price_from_goldapiio():
  api_key = os.environ["GOLDAPIIO_API_KEY"]
  url = "https://www.goldapi.io/api/XAU/USD"
  headers = {
    "x-access-token": api_key
  }

  response = requests.get(url, headers=headers)
  data = response.json()

  # {
  #   'timestamp': 1716341513, 
  #   'metal': 'XAU', 
  #   'currency': 'USD', 
  #   'exchange': 'FOREXCOM', 
  #   'symbol': 'FOREXCOM:XAUUSD', 
  #   'prev_close_price': 2421.045, 
  #   'open_price': 2421.045, 
  #   'low_price': 2419.93, 
  #   'high_price': 2423.48, 
  #   'open_time': 1716336000, 
  #   'price': 2420.95, 
  #   'ch': -0.1, 
  #   'chp': 0.01, 
  #   'ask': 2421.27, 
  #   'bid': 2420.54, 
  #   'price_gram_24k': 77.8353, 
  #   'price_gram_22k': 71.3491, 
  #   'price_gram_21k': 68.1059, 
  #   'price_gram_20k': 64.8628, 
  #   'price_gram_18k': 58.3765, 
  #   'price_gram_16k': 51.8902, 
  #   'price_gram_14k': 45.404, 
  #   'price_gram_10k': 32.4314
  # }

  return {
    "timestamp": data["timestamp"],
    "price": data["price"]
  }

