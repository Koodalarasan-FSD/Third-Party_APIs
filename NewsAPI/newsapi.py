from flask import Flask, render_template
import requests

app = Flask(__name__)

#https://newsapi.org/account
#Login Password-Koodal@7598

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = 'c13e40503d664645833c1187f5a8b0e3'
base_url= f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}'



@app.route('/')
def index():
    try:
        # Fetch top headlines from the News API
        response=requests.get(base_url)
        response.raise_for_status()     # Check for HTTP errors
        news_data=response.json()
        articles=news_data['articles']
        return render_template('newsapi.html',articles=articles)
    except requests.exceptions.RequestException as e:
        return f'Error fetching news data: {str(e)}'
    

if __name__=='__main__':
    app.run(debug=True)