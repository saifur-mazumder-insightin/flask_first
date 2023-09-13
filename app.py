from unicodedata import name
from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"


@app.route('/marks/<int:score>')
def pass_fail(score):

    if score > 50:
        results = 'Pass'
     
    else:
        results = 'Fail'

    return(results)


@app.route('/ID/<int:id>')
def first_app(id):

    if id == 1:
        return jsonify({'Name': 'MD Saifur',
                    'email': 'smazumder@insightintechnology.com',
                    'message': 'Good Morning'}
                    )

    else:
        return jsonify({'Name': 'David Silva',
                    'email': 'smazumder@insightintechnology.com',
                    'message': 'Good night'}
                   )


if __name__ == '__main__':
    app.run(debug = True)









