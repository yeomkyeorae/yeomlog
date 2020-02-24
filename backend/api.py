from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
import pymysql
# from dbController import CreateUser

app = Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/interest/<int:category_id>', methods=['GET'])
def interests(category_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM interests WHERE category_id=%s", category_id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    

class CreateInterest(Resource):
    def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument('category_id', type=int)
            parser.add_argument('title', type=str)
            parser.add_argument('content', type=str)
            args = parser.parse_args()

            _category_id = args['category_id']
            _title = args['title']
            _content = args['content']
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_create_interest', (_category_id, _title, _content))
            data = cursor.fetchall()
 
            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'Interest creation success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}


mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'yeomlog'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

api.add_resource(CreateInterest, '/interest')

if __name__ == '__main__':
    app.run(debug=True)
