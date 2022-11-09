from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from send_email import send_mail_test
from bleach import clean
import os


app = Flask(__name__)

ENV = 'prod'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:paopow123@localhost:5433/manila'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    feedback = db.Column(db.Text())

    def __init__(self, customer, rating, feedback):
        self.customer = customer
        self.rating = rating
        self.feedback = feedback


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = clean(request.form['customer'])
        rating = clean(request.form['rating'])
        feedback = clean(request.form['feedback'])
        if customer == '' or feedback == '':
            return render_template('form.html', message='Please fill out ALL required fields')
        
        user_data = Review(customer, rating, feedback)
        db.session.add(user_data)
        db.session.commit()
        send_mail_test(customer, rating, feedback)
        return render_template('submitted.html')

if __name__ == '__main__':
    app.run()