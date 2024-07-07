import requests
from configs.celery import app


@app.task
def get_exchange_rates():
    print('Getting exchange rates')
    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
    if response.status_code == 200:
        rates = response.json()
        exchange_rates = {
            'USD': 1.0,
            'EUR': 1.0,
            'UAH': 1.0
        }
        for rate in rates:
            if rate['ccy'] == 'USD':
                exchange_rates['USD'] = float(rate['sale'])
            elif rate['ccy'] == 'EUR':
                exchange_rates['EUR'] = float(rate['sale'])
        return exchange_rates
    return {
        'USD': 1.0,
        'EUR': 1.0,
        'UAH': 1.0
    }
