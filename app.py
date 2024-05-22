import metals_api

def main():
  print("You're running the commodity news app.\n\n")

  demo_metals_apis()

def demo_metals_apis():
  print("Metalprice API:")
  print(str(metals_api.get_current_gold_price_from_metalpricesapi()))
  print("")

  print("GoldIO API:")
  print(str(metals_api.get_current_gold_price_from_goldapiio()))
  print("")

if __name__ == "__main__":
  main()

