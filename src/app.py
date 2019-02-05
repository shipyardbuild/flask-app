from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    print('I like Python!', flush=True)
    return 'Hello, world!'
