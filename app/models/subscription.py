import mysql.connector
from connection import db


def new(user_id, query_id):
    if check_subscription(user_id, query_id):
        return False
    cursor = db.cursor()
    sql = 'INSERT INTO subscriptions (UserId, QueryId) VALUES (%s, %s)'
    val = (user_id, query_id)

    try:
        cursor.execute(sql, val)
        db.commit()
    except mysql.connector.Error as err:
        print(f'Err: {err}')
        db.rollback()
    return True


def check_subscription(user_id, query_id):
    cursor = db.cursor()
    sql = 'SELECT * FROM subscriptions WHERE (UserId, QueryId) = (%s, %s)'
    val = (user_id, query_id)
    cursor.execute(sql, val)
    result = cursor.fetchone()

    if result:
        return True
    return False


def get_for_user(user_id):
    cursor = db.cursor()
    sql = 'SELECT * FROM subscriptions WHERE UserId = %s'
    val = (user_id, )
    cursor.execute(sql, val)
    result = cursor.fetchall()

    return create_dict(result)


def get_for_query(query_id):
    cursor = db.cursor()
    sql = 'SELECT * FROM subscriptions WHERE QueryId = %s'
    val = (query_id, )
    cursor.execute(sql, val)
    result = cursor.fetchall()

    return create_dict(result)


def create_dict(result):
    ret = []
    for r in result:
        o = {
            'id': r[0],
            'user_id': r[1],
            'query_id': r[2]
        }
        ret.append(o)
    return ret
