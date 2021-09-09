from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User_Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)