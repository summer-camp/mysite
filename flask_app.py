from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html', the_heading="Hello")

@app.route('/start')
def start():
    return 'Lets start a new game!'

@app.route('/choose/<letter>')
def choose(letter):
    # show the user profile for that user
    return 'The letter you choose is %s' % letter
