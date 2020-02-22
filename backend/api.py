from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
# from dbController import CreateUser

app = Flask(__name__)
api = Api(app)

# @app.route('/scheduler', methods=['GET', 'POST'])
# def scheduler():
#     if request.method == 'GET':
#         start = request.args.get('start')
#         end = request.args.get('end')

#         return db.getInterests({'start': start, 'end': end})

#     if request.method == 'POST':
#         start = request.form['start']
#         end = request.form['end']
#         title = request.form['title']
#         allDay = request.form['allDay']

#         schedule = {'title': title, 'start': start, 'end': end, 'allDay': allDay}

#         return db.setInterests(schedule)

class CreateUser(Resource):
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
app.config['MYSQL_DATABASE_DB'] = 'interests'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

api.add_resource(CreateUser, '/user')

if __name__ == '__main__':
    app.run(debug=True)
