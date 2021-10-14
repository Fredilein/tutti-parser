from connection import db


def get_all():
    cursor = db.cursor()
    sql = 'SELECT * FROM queries'
    cursor.execute(sql)
    result = cursor.fetchall()

    return create_dict(result)


def create_dict(result):
    ret = []
    for r in result:
        o = {
            'id': r[0],
            'query': r[1]
        }
        ret.append(o)
    return ret
