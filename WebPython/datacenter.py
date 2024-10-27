import sqlite3


def takedata(lenh):  # lenh truy van sql
    with sqlite3.connect('WebPython/data.db') as conn:
        c = conn.cursor()
        c.execute(lenh)
        respon = c.fetchall()
        return respon


def pushdata(lenh):  # lenh truy van sql
    with sqlite3.connect('WebPython/data.db') as conn:
        c = conn.cursor()
        c.execute(lenh)
        conn.commit()
        return True
