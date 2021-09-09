from flask import Flask, make_response

app=Flask(__name__)


@app.route('/')
def index():
    response = make_response('<h1>This document gives you cookies!</h1>')
    response.set_cookie('jy', '23')
    return response, 200