import mysql.connector

# Rename this file to connection.py and
# Use your own credentials

db = mysql.connector.connect(
    host='localhost',
    user='USERNAME',
    password='PASSWORD',
    port=3306,
    database='DBNAME'
)