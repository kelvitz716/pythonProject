import requests
import json

def get_usd_to_kes_exchange_rate():
    # Replace 'YOUR_APP_ID' with your actual Open Exchange Rates API App ID
    app_id = 'de4820393fbb4942bf015d2d7fa4f605'
    base_url = f'https://openexchangerates.org/api/latest.json?app_id={app_id}'

    response = requests.get(base_url)
    data = response.json()

    if 'rates' in data and 'KES' in data['rates']:
        usd_to_kes_rate = data['rates']['KES']
        return usd_to_kes_rate
    else:
        return None

def main():
    usd_to_kes_rate = get_usd_to_kes_exchange_rate()

    if usd_to_kes_rate is not None:
        print(f'1 USD = {usd_to_kes_rate} KES')
    else:
        print('Unable to fetch exchange rate.')

if __name__ == '__main__':
    main()
