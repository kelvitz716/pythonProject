import requests
import json

def get_exchange_rate():
    #Gets the current exchange rate for USD to Kes.
    url = 'http://api.exchangeratesapi.io/v1/latest?access_key=6fb9394e1e00a152155ad254791ac37b'
   
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content)
        if "rates" in data:
            return data["rates"]["KES"]
        else:
            raise Exception("Could not find exchange rate for KES.")
    else:
        raise Exception("Could not get exchange rate.")
    

def main():
    #The main function.
    exchange_rate = get_exchange_rate()
    print(f"1 USD is equal to {exchange_rate} KES.")

if __name__ == "__main__":
    main()
