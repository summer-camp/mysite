from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return 'Here is a new line!'
