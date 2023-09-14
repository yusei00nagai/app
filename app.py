import json
import pymysql
from flask import Flask

app = Flask(__name__)

@app.route('/')
def getConnection():
    return pymysql.connect(
        host='localhost',
        user='app',
        password='app',
        database='app',
        cursorclass=pymysql.cursors.DictCursor)

@app.route('/users')
def users():
    connection = getConnection()
    with connection:
       with connection.cursor() as cursor:
            sql = "SELECT * FROM `user`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps(result)
       
@app.route('/')
def hello():
    return "<h1>Hello Flask</h1>\n"

if __name__ == "__main__":
     app.run(debug=True, host='0.0.0.0')
