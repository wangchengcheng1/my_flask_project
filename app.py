from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)

HOSTNAME = 'localhost'
PORT = '3306'
DATABASE = 'learn'
USERNAME = 'root'
PASSWORD = '123456'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'

db=SQLAlchemy(app)


with app.app_context():
    try:
        with db.engine.connect() as conn:
            print("尝试连接数据库...")
            rs = conn.execute(text('select 1'))
            result = rs.fetchone()
            print(f"数据库连接成功，结果：{result}")
    except Exception as e:
        print(f"数据库连接错误：{str(e)}")


@app.route('/')
def home():
    return 'Hello, Flask!1'

@app.route('/about/<int:about_id>')
def about(about_id):
    return f'About Flask! {about_id}'

if __name__ == '__main__':
    app.debug = True
    app.run()
