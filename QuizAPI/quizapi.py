from flask import Flask, render_template, request, redirect, url_for, session
import requests
import random

app = Flask(__name__)

# Open Trivia Database API endpoint for fetching questions
API_URL = "https://opentdb.com/api.php"

@app.route('/')
def start_quiz():
    return render_template('quiz.html', error=None)

@app.route('/start_quiz', methods=['POST'])
def initialize_quiz():
    category = request.form.get('category')
    difficulty = request.form.get('difficulty')
    num_questions = int(request.form.get('num_questions'))

    # Make API request to fetch quiz questions
    params = {
        'amount': num_questions,
        'category': category,
        'difficulty': difficulty,
        'type': 'multiple'  # Multiple-choice questions
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    if response.status_code != 200 or data['response_code'] != 0:
        return render_template('quiz.html', error='Error fetching quiz questions. Please try again.')

    questions = data['results']

    # Store fetched questions in session for later retrieval
    session['quiz_questions'] = questions

    return redirect(url_for('display_questions'))

@app.route('/display_questions')
def display_questions():
    questions = session.get('quiz_questions')

    if not questions:
        return redirect(url_for('start_quiz'))

    return render_template('quiz_questions.html', questions=questions)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    questions = session.get('quiz_questions')

    if not questions:
        return redirect(url_for('start_quiz'))

    # Initialize score
    score = 0

    for idx, question in enumerate(questions):
        selected_option = request.form.get(f'question_{idx + 1}')

        # Check if the selected option is correct
        if selected_option == question['correct_answer']:
            score += 1

    # Clear stored questions from session
    session.pop('quiz_questions', None)

    return render_template('quiz_results.html', score=score)

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'  # Set a secret key for session
    app.run(debug=True)
