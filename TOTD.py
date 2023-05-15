""" Introduction:
Course: CST 205 Section 1 - Multimedia Design & Programming

Title: TOTD (TRENDS OF THE DAY)

Abstract: This is a flask app to show daily trends of the top 
platforms on the internet to enhance marketing.

Authors: Aaron Johnson, Eunice Sosa, Sebastian Ramos, Mikaela Lagumbay

Date: May 18, 2023

Work by Aaron Johnson:
1. Researched and found Trend info for several platforms
2. Created the flask app
3. Created the basic structure of the index.html file
4. Used some boostrap to make the website look better

Work by Eunice Sosa:
1. Researched and found Trend info for several platforms

Work by Sebastian Ramos:
1. Researched and found Trend info for several platforms

Work by Mikaela Lagumbay:
1. Researched and found Trend info for several platforms

"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')