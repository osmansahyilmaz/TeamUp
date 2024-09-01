import mysql.connector
from mysql.connector import errorcode
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='test',
            user='root',
            password='616161.Oo'
        )
        
        print("Connection to MySQL DB successful")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return connection
