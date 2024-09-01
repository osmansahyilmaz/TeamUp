# cursor_utils.py
import mysql.connector
from mysql.connector import errorcode
from connect import create_connection

def execute_query(query, params=None):
    cnx = create_connection()
    cursor = cnx.cursor()
    try:
        cursor.execute(query, params)
        cnx.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        cnx.close()

def fetch_all(query, params=None):
    cnx = create_connection()
    cursor = cnx.cursor()
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        cnx.close()