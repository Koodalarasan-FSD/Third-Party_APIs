from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_OPENEXCHANGERATES_API_KEY' with your actual API key
api_key = '6d7a0937b67a917e9c9e735b'

#https://app.exchangerate-api.com/dashboard
#Login Password--Koodal@7598
#https://www.exchangerate-api.com/


@app.route('/')
def index():
    return render_template('index_currency_api.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        base_url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}'

        # Fetch the latest exchange rates
        response = requests.get(base_url)
        print(response)
        data = response.json()
        print(data)
        rates = data['conversion_rates']
       

        # Check if the currencies are valid
        if from_currency not in rates or to_currency not in rates:
            return render_template('index_currency_api.html', error='Invalid currency selection.')

        # Perform the currency conversion
        converted_amount = amount * rates[to_currency] / rates[from_currency]

        return render_template('index_currency_api.html', result=f'{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.')
    except Exception as e:
        return render_template('index_currency_api.html', error=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
