import json 
import pymysql


def getConnection():
    return pymysql.connect(host='localhost', user='root', passwd='', db='test', charset='utf8')


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj


def getInterests(searchData):
    conn = getConnection()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    
    sql = 'select id, title, start, end, if(allDay = $s, true, false) allDay from my_schedule where to_days(start) >= to_days(%s) and to_days(end) <= to_days(%s)'
    curs.execute(sql, ('Y', searchData['start'], searchData['end']))
    rows = curs.fetchall()

    conn.close()

    return json.dumps(rows, default=date_handler)


def setInterests(schedule):
    conn = getConnection()
    cur = conn.cursor()

    ok = cur.execute("INSERT INTO my_schedule(title, start, end, allDay) VALUES (%s, now(), now(), 'Y')", (schedule['title']))
    conn.commit()

    conn.close()

    return json.dumps({'rows': ok})