from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Pull Request, gotta get her to work! 2nd commit'
