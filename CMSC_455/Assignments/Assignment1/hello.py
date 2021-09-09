from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.core import IntegerField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'you will never get this'

class OverrideForm(FlaskForm):
    student_id = IntegerField("Enter your V-number (Do not include the V in your Student Number)", validators=[DataRequired()])
    name = StringField("Enter your full name", validators=[DataRequired()])
    email = StringField("Enter your VCU Email Address", validators=[DataRequired()])
    course = StringField("Enter the course number that you wish to override", validators=[DataRequired()])
    section = IntegerField("Enter the section number you wish to override", validators=[DataRequired()])
    crn = IntegerField("Enter the CRN for the course you wish to override", validators=[DataRequired()])
    comments = StringField("Comments")
    submit = SubmitField("Submit")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form_page():
    form = OverrideForm()
    if form.validate_on_submit():
        return redirect("/form/submitted")
    return render_template('form_page.html', form=form)

@app.route("/form/submitted")
def form_submitted():
    return render_template('form_submitted.html')

@app.errorhandler(404)
def page_handler(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_handler(e):
    return render_template('500.html'), 500
