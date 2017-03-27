from flask import redirect
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask_babel import Babel
from werkzeug.routing import BuildError

app = Flask(__name__)
babel = Babel(app)

SUPPORTED_LANGUAGES = ['en', 'es', 'fr']

@babel.localeselector
def get_locale():
    return request.cookies.get('LANGUAGE', 'en')

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/2')
def two():
    return render_template('two.html')

@app.route('/3')
def three():
    return render_template('three.html')

@app.route('/lang/<language>')
def select_language(language):
    url = '/'
    endpoint = request.args.get('camefrom')
    if endpoint is not None:
        try:
            url = url_for(endpoint)
        except BuildError:
            pass
    response = redirect(url)
    if language in SUPPORTED_LANGUAGES:
        response.set_cookie('LANGUAGE', language)
    return response
