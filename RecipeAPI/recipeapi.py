# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#https://www.edamam.com/
#Login Password- Koodal@7598

@app.route('/')
def index():
    return render_template('recipeapi.html')

@app.route('/getrecipe', methods=['GET', 'POST'])
def getrecipe():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        if search_query:
            # Replace 'YOUR_APP_ID' and 'YOUR_API_KEY' with your Edamam API credentials
            app_id = '95e0fcc5'  #Recipe Search ID
            app_key = 'e3f45006f0a2e54f27f9b73cbcabda6d'  #Recipe Search API
            api_url = f'https://api.edamam.com/search?q={search_query}&app_id={app_id}&app_key={app_key}'

            try:
                response = requests.get(api_url)
                response.raise_for_status()
                recipe_data = response.json()
                recipes = recipe_data.get('hits', [])
                return render_template('recipeapi.html', recipes=recipes)
            except requests.exceptions.RequestException as e:
                return f'Error fetching recipe data: {str(e)}'

    return render_template('recipeapi.html', recipes=[])

if __name__ == '__main__':
    app.run(debug=True)
