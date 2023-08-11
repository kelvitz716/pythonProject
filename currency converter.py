import requests

def get_exchange_rate():
    # Replace 'API_KEY' with your actual API key
    api_key = '6fb9394e1e00a152155ad254791ac37b'

    # The exchange rate endpoint
    url = 'http://api.exchangeratesapi.io/v1/convert'

    # The parameters for the API call
    params = {
        'access_key': api_key,
        'from': 'GBP',
        'to': 'JPY',
        'amount': '25',
        'date' : '2023-08-11'
    }

    # Make the API call
    response = requests.get(url, params=params)

    # Check the response status code
    if response.status_code == 200:
        # The API call was successful
        data = response.json()

        # Get the exchange rate
        exchange_rate = data['rates']['JPY']

        # Print the exchange rate
        print(f'The exchange rate for 25 GBP is {exchange_rate} JPY')

    else:
        # The API call failed
        print(f'API call failed with status code {response.status_code}')

if __name__ == '__main__':
    get_exchange_rate()
