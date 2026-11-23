import pymysql

def get_connection():

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password="0000",
        database="pythondb"
    );

    return connection
