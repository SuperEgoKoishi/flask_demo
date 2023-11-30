import pymysql


def create_database():
    db_connect = pymysql.Connect(host="localhost", port=3306, user="root", password="Nanahirasuki#233")
    cursor = db_connect.cursor()
    result = cursor.execute("CREATE DATABASE database1")
    print(result)
    result = cursor.fetchone()
    print(result)
    cursor.close()
    db_connect.close()


def create_table():
    db_connect = pymysql.Connect(host="localhost", port=3306, user="root", password="Nanahirasuki#233")
    cursor = db_connect.cursor()
    result = cursor.execute("CREATE DATABASE database1")
    print(result)
    result = cursor.fetchone()
    print(result)
    cursor.close()
    db_connect.close()


if __name__ == '__main__':
    create_database()
