# import json 
# import pymysql


# def getConnection():
#     return pymysql.connect(host='localhost', user='root', passwd='', db='test', charset='utf8')


# def date_handler(obj):
#     return obj.isoformat() if hasattr(obj, 'isoformat') else obj


# def getInterests(searchData):
#     conn = getConnection()
#     curs = conn.cursor(pymysql.cursors.DictCursor)
    
#     sql = 'select id, title, start, end, if(allDay = $s, true, false) allDay from my_schedule where to_days(start) >= to_days(%s) and to_days(end) <= to_days(%s)'
#     curs.execute(sql, ('Y', searchData['start'], searchData['end']))
#     rows = curs.fetchall()

#     conn.close()

#     return json.dumps(rows, default=date_handler)


# def setInterests(schedule):
#     conn = getConnection()
#     curs = conn.cursor()

#     ok = cur.execute("INSERT INTO my_schedule(title, start, end, allDay) VALUES (%s, now(), now(), 'Y')", (schedule['title']))
#     conn.commit()

#     conn.close()

#     return json.dumps({'rows': ok})
from flask_restful import Resource


class CreateUser(Resource):
    def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('username', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()
 
            _userEmail = args['email']
            _userName = args['username']
            _userPassword = args['password']
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_create_user', (_userEmail, _userName, _userPassword))
            data = cursor.fetchall()
 
            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'User creation success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}