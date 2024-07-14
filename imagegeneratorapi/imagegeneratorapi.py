from flask import Flask, render_template
import requests

app = Flask(__name__)

# Define API endpoints for cat and dog images
CAT_API_URL = "https://api.thecatapi.com/v1/images/search"
DOG_API_URL = "https://dog.ceo/api/breeds/image/random"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_cat')
def random_cat():
    response=requests.get(CAT_API_URL)
    cat_data=response.json()
    
    image_url=cat_data[0]['url']
    return render_template('random_image.html',image_url=image_url)

@app.route('/random_dog')
def random_dog():
    response=requests.get(DOG_API_URL)
    dog_data=response.json()

    image_url=dog_data['message']
    return render_template('random_image.html',image_url=image_url)

if __name__=="__main__":
    app.run(debug=True)