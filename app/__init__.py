from flask import redirect
from flask import Flask
from flask import render_template
from flask import request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

SUPPORTED_LANGUAGES = ['en', 'es', 'fr']

@babel.localeselector
def get_locale():
    return request.cookies.get('LANGUAGE', 'en')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/lang/<language>')
def select_language(language):
    response = redirect('/')
    if language in SUPPORTED_LANGUAGES:
        response.set_cookie('LANGUAGE', language)
    return response
