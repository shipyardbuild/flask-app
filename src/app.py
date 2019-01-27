from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world. SELF PR, update of PR on self'
