from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db=SQLAlchemy(app)

@app.route('/')
def home():
    return 'Hello, Flask!1'

@app.route('/about/<int:about_id>')
def about(about_id):
    return f'About Flask! {about_id}'

if __name__ == '__main__':
    app.run(debug=True)
