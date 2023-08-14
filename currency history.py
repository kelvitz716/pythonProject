import requests

def get_exchange_rates():
    # Replace 'API_KEY' with your actual API key
    api_key = '6fb9394e1e00a152155ad254791ac37b'

    # The exchange rate endpoint
    url = 'http://api.exchangeratesapi.io/v1/2022-12-24'

    # The parameters for the API call
    params = {
        'access_key': api_key,
        'base': 'GBP',
        'symbols': 'USD,CAD,EUR'
    }

    # Make the API call
    response = requests.get(url, params=params)

    # Check the response status code
    if response.status_code == 200: 
        # The API call was successful
        data = response.json()

        # Get the exchange rates
        exchange_rates = data['rates']

        # Print the exchange rates
        for symbol, rate in exchange_rates.items():
            print(f'{symbol}: {rate}')

    else:
        # The API call failed
        error_info = response.json().get('error', {}).get('info', 'Unknown Error')
        print(f'API call failed with status code {response.status_code}: {error_info}')

if __name__ == '__main__':
    get_exchange_rates()
