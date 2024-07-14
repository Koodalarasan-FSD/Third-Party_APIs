# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#https://www.edamam.com/
#Login Password- Koodal@7598

@app.route('/')
def index():
    return render_template('food_databaseapi.html')

@app.route('/getfood', methods=['GET', 'POST'])
def getfood():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if search_query:
            # Replace 'YOUR_APP_ID' and 'YOUR_API_KEY' with your Edamam API credentials
            app_id = '87f3fe95'  #Food Database ID
            app_key = 'c15ec6ead190adf84bafcf98793b62fd'  #Food Database API
            api_url = f'https://api.edamam.com/api/food-database/v2/parser?ingr={search_query}&app_id={app_id}&app_key={app_key}'

            try:
                response = requests.get(api_url)
                response.raise_for_status()
                food_data = response.json()
                foods = food_data.get('hints', [])
                return render_template('food_databaseapi.html', foods=foods)
            except requests.exceptions.RequestException as e:
                return f'Error fetching recipe data: {str(e)}'

    return render_template('food_databaseapi.html', foods=[])

if __name__ == '__main__':
    app.run(debug=True)
