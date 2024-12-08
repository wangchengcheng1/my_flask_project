from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_demo'
USERNAME = 'root'
PASSWORD = 'root'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'

db=SQLAlchemy(app)

@app.route('/')
def home():
    return 'Hello, Flask!1'

@app.route('/about/<int:about_id>')
def about(about_id):
    return f'About Flask! {about_id}'

if __name__ == '__main__':
    app.run(debug=True)
