from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Here is a new line!'

@app.route('/start')
def start():
    return 'Lets start a new game!'
