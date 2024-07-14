from flask import Flask,jsonify, render_template
import requests
 
app = Flask(__name__)

# Define the JokeAPI URL
JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"


@app.route('/')
def index():
    return render_template('jokegeneratorapi.html')

@app.route('/get_random_joke',methods=['GET','POST'])
def get_random_joke():

    try:
        # Fetch a random joke from the JokeAPI
        response= requests.get(JOKE_API_URL)
        response.raise_for_status()
        joke_data=response.json()

        #check if the response contains a joke setup and delivery
        if 'setup' in joke_data and 'delivery' in joke_data:
            joke={
                'setup':joke_data['setup'],
                'delivery':joke_data['delivery']
            }

        elif 'joke' in joke_data:
            joke={
                'joke':joke_data['joke']
            }    

        else:
            return jsonify({'error':'Failed to fetch a valid joke'}), 500
        
        return jsonify(joke)
    except requests.exceptions.RequestException as e:
        return jsonify({'error':f'Error fetching joke data:{str(e)}'}),500
    

if __name__=='__main__':
    app.run(debug=True) 