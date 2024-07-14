from flask import Flask, jsonify, request,render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('loginusingapi.html')

# Define an API endpoint to check if name and email exist
@app.route('/check_user', methods=['POST'])
def check_user():
    email = request.form['email']
    password = request.form['password']

    if not email or not password:
        return jsonify({'error': 'Both email and password are required'}), 400

    # Fetch API data from the provided URL
    api_url = 'https://koodalarasan-fsd.github.io/apihosting2/hostingapi2.json'
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for HTTP errors
        api_data = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching API data: {str(e)}'}), 500

    
    matching_users = []
    
    # Check if the provided email and password exist in the fetched data
    for user in api_data:
        if user.get('email') == email and user.get('password') == password:           #user.get('') will get data from api
            matching_user = {
                'name': user.get('name'),
                'email': user.get('email'),
                'street': user.get('address', {}).get('street'),  #address contains another set of datas with it that's why using {}, check in api datas
                'city': user.get('address', {}).get('city'),
                'zipcode': user.get('address', {}).get('zipcode'),
            }
            matching_users.append(matching_user)
        
            


    if matching_users:
        return jsonify({'exists': True, 'user': matching_users[0]})
    else:
        return jsonify({"Warning":"E-Mail or Password is wrong",'exists': False})

if __name__ == '__main__':
    app.run(debug=True)
