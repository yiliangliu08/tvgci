import os

from flask import Flask, render_template
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run()
