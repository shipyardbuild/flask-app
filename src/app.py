from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    print('I like python', flush=True)
    return 'wowsers'
