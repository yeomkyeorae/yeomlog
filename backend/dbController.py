import pymysql


db = pymysql.connect(host='localhost', user='root', passwd='', db='test', charset='utf8')
cursor = db.cursor()
sql = """
    CREATE TABLE korea (
           id INT UNSIGNED NOT NULL AUTO_INCREMENT,
           name VARCHAR(20) NOT NULL,
           model_num VARCHAR(10) NOT NULL,
           model_type VARCHAR(10) NOT NULL,
           PRIMARY KEY(id)
    );
    """
cursor.execute(sql)
db.commit()
db.close()