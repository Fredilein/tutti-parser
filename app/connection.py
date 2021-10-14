import mysql.connector
from time import sleep

sleep(15)

db = mysql.connector.connect(
    host='db',
    user='root',
    password='root',
    port=3306,
    database='tutti'
)