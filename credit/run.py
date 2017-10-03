from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, app, Credit

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:xtian211@localhost:5432/creditdb' 

@app.route("/")
def index():
    return render_template('index.html', credit = Credit.query.all())

@app.route("/search", methods=['GET', 'POST'])
def search():
	text = request.form['query']
	credits = Credit.query.filter_by(id=text).first_or_404()
	
	return render_template('results.html', credits=credits)

if __name__ == '__main__':
    app.run()