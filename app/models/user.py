import mysql.connector
from connection import db


def new(chat_id):
    exists = get_from_chat_id(chat_id)
    if exists:
        return

    cursor = db.cursor()
    sql = 'INSERT INTO users (ChatId) VALUES (%s)'
    val = (chat_id, )

    try:
        cursor.execute(sql, val)
        db.commit()
    except mysql.connector.Error as err:
        print(f'Err: {err}')
        db.rollback()


def get_all():
    cursor = db.cursor()
    sql = 'SELECT * FROM users'
    cursor.execute(sql)
    result = cursor.fetchall()

    return create_dict(result)


def get_user(user_id):
    cursor = db.cursor()
    sql = 'SELECT * FROM users WHERE Id = %s'
    val = (user_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result:
        return {
            'id': result[0],
            'chat_id': result[1]
        }
    return None


def get_from_chat_id(chat_id):
    cursor = db.cursor()
    sql = 'SELECT * FROM users WHERE ChatId = %s'
    val = (chat_id, )
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result:
        return {
            'id': result[0],
            'chat_id': result[1]
        }
    return None


def create_dict(result):
    ret = []
    for r in result:
        o = {
            'id': r[0],
            'chat_id': r[1]
        }
        ret.append(o)
    return ret
