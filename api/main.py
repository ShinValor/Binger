from flask import Flask, Response, render_template


app = Flask(__name__)


#   Read env variables from config.py
app.config.from_object('config.Config')

#   Testing if it worked
@app.route('/')
def home():
    return render_template('index.html')