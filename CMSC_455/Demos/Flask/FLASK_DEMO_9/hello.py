from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtform.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY'] = "lalalalala you will never get this"

bootstrap = Bootstrap(app)
moment = Moment(app)
