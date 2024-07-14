from flask import Flask, render_template,request
import requests

app = Flask(__name__)

#https://newsapi.org/account
#Login Password-Koodal@7598

# Replace 'YOUR_API_KEY' with your actual News API key
api_key = 'c13e40503d664645833c1187f5a8b0e3'


@app.route('/')
def index():
    return render_template('newsapi_forparticularcountry.html')

@app.route('/getnews',methods=['POST'])
def getnews():
    Country=request.form['countryname']
    
    try:
        base_url= f'https://newsapi.org/v2/top-headlines?country={Country}&apiKey={api_key}'
        
        # Fetch top headlines from the News API
        response=requests.get(base_url)
        response.raise_for_status()     # Check for HTTP errors
        news_data=response.json()
        articles=news_data['articles']
        return render_template('newsapi_forparticularcountry.html',articles=articles)
    except requests.exceptions.RequestException as e:
        return f'Error fetching news data: {str(e)}'
    

if __name__=='__main__':
    app.run(debug=True)