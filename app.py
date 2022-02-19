import os
import uuid

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://thhdiqjopereve:c43e9cd76448f496e9508a5ad704520d43bc30d795275396d94543749485f603@ec2-44-193-188-118.compute-1.amazonaws.com:5432/d1es6b77cis6gd'
db = SQLAlchemy(app)


class customers(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    name = db.Column(db.String(30))
    email = db.Column(db.String(30))
    phone = db.Column(db.String(15))
    budget = db.Column(db.Float)
    comment = db.Column(db.String(1024))
    status = db.Column(db.String(16), default="received")

    def __init__(self, name, email, phone, budget, comment):
        self.name = name
        self.email = email
        self.phone = phone
        self.budget = budget
        self.comment = comment

db.create_all()

@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/partner')
def partner():
    return render_template('partner.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/showcase')
def showcase():
    hists = os.listdir('static/image/mocha')
    hists = ['image/mocha/' + file for file in hists]
    return render_template('showcase.html', hists=hists)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method =='POST':
        print(request.form['name'])
        customer = customers(request.form['name'], request.form['email'], request.form['phone'], request.form['budget'], request.form['comment'])
        db.session.add(customer)
        db.session.commit()
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
