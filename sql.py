import sqlite3
import os
from pathlib import Path
import pymysql

conn = None
cursor = None
db_type = None


def _execute(sql, params=None):
    global db_type
    if db_type == 'sqlite':
        sql = sql.replace('%s', '?')
    elif db_type == 'mysql':
        sql = sql.replace('?', '%s')
    if params is not None:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)


def _init_sqlite_tables():
    _execute('''
        CREATE TABLE IF NOT EXISTS people (
            name TEXT PRIMARY KEY,
            password TEXT,
            job TEXT,
            class TEXT
        )
    ''')
    _execute('''
        CREATE TABLE IF NOT EXISTS sports (
            sport TEXT PRIMARY KEY
        )
    ''')
    _execute('''
        CREATE TABLE IF NOT EXISTS sporter (
            name TEXT,
            class TEXT,
            sport1 TEXT,
            sport2 TEXT,
            sport3 TEXT,
            id INTEGER
        )
    ''')
    _execute('''
        CREATE TABLE IF NOT EXISTS ranking_classes_7 (
            class TEXT PRIMARY KEY,
            scroe INTEGER,
            ranking INTEGER
        )
    ''')
    _execute('''
        CREATE TABLE IF NOT EXISTS ranking_classes_8 (
            class TEXT PRIMARY KEY,
            scroe INTEGER,
            ranking INTEGER
        )
    ''')
    _execute('''
        CREATE TABLE IF NOT EXISTS ranking_classes_9 (
            class TEXT PRIMARY KEY,
            scroe INTEGER,
            ranking INTEGER
        )
    ''')
    _execute('''
        CREATE TABLE IF NOT EXISTS ranking_sporters (
            sporter_name TEXT,
            sporter_id INTEGER,
            sporter_class TEXT,
            sporter_ranking INTEGER,
            sport TEXT,
            sports_scroe INTEGER,
            UNIQUE(sporter_name, sport)
        )
    ''')

    _execute("SELECT COUNT(*) FROM people")
    if cursor.fetchone()[0] == 0:
        _execute("INSERT INTO people (name, password, job) VALUES (?, ?, ?)", ('1949', '1001', '总控'))

    _execute("SELECT COUNT(*) FROM sports")
    if cursor.fetchone()[0] == 0:
        _execute("INSERT INTO sports (sport) VALUES (?)", (' ',))

    conn.commit()


def start():
    global conn, cursor, db_type
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='Lin20130',
            database='新纪元',
            connect_timeout=3
        )
        cursor = conn.cursor()
        db_type = 'mysql'
        print("[数据库] 已连接 MySQL")
        _init_sqlite_tables()
        return conn
    except Exception as e:
        print(f"[数据库] MySQL 连接失败: {e}")
        print("[数据库] 正在切换到 SQLite...")
    
    db_dir = Path(__file__).parent / 'SQL'
    db_dir.mkdir(exist_ok=True)
    db_path = db_dir / 'sport.db'
    
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    db_type = 'sqlite'
    _init_sqlite_tables()
    print(f"[数据库] 已连接 SQLite: {db_path}")
    return conn

def add_zhuce(name, password, job, class_):
    _execute(
        "INSERT INTO people (name, password, job, class) VALUES (%s, %s, %s, %s)",
        (name, password, job, class_)
    )
    conn.commit()

def add_denglu(name, password):
    _execute(
        "SELECT * FROM people WHERE name = %s AND password = %s",
        (name, password)
    )
    return cursor.fetchone()

def find_sports():
    _execute("SELECT sport FROM sports")
    return cursor.fetchall()

def add_sports(name):
    _execute('INSERT INTO sports (sport) VALUES (%s)', (name,))
    conn.commit()

def add_sporter(name, class_, sport1, sport2, sport3, id):
    _execute(
        'INSERT INTO sporter (name, class, sport1, sport2, sport3, id) VALUES (%s, %s, %s, %s, %s, %s)',
        (name, class_, sport1, sport2, sport3, id)
    )
    conn.commit()

def find_class(name):
    _execute("SELECT * FROM people WHERE name = %s", (name,))
    res = cursor.fetchone()
    return res[3] if res else ""

def find_class_(name):
    _execute("SELECT * FROM sporter WHERE name = %s", (name,))
    res = cursor.fetchone()
    return res[1] if res else ""

def add_grade(name, id, class_, ranking, sport, scroe):
    _execute(
        'INSERT INTO ranking_sporters (sporter_name, sporter_id, sporter_class, sporter_ranking, sport, sports_scroe) VALUES (%s, %s, %s, %s, %s, %s)',
        (name, id, class_, ranking, sport, scroe)
    )
    conn.commit()

def find_sporter(sports):
    _execute(
        "SELECT * FROM sporter WHERE sport1 = %s OR sport2 = %s OR sport3 = %s",
        (sports, sports, sports)
    )
    result_all = cursor.fetchall()
    result = [row[0] for row in result_all]
    return result

def add_7(class_, scroe=0, ranking=None):
    _execute(
        'INSERT INTO ranking_classes_7 (class, scroe, ranking) VALUES (%s, %s, %s)',
        (class_, scroe, ranking)
    )
    conn.commit()

def add_8(class_, scroe=0, ranking=None):
    _execute(
        'INSERT INTO ranking_classes_8 (class, scroe, ranking) VALUES (%s, %s, %s)',
        (class_, scroe, ranking)
    )
    conn.commit()

def add_9(class_, scroe=0, ranking=None):
    _execute(
        'INSERT INTO ranking_classes_9 (class, scroe, ranking) VALUES (%s, %s, %s)',
        (class_, scroe, ranking)
    )
    conn.commit()

def update_7(class_, scroe, ranking):
    _execute(
        'UPDATE ranking_classes_7 SET scroe = %s, ranking = %s WHERE class = %s',
        (scroe, ranking, class_)
    )
    conn.commit()

def update_8(class_, scroe, ranking):
    _execute(
        'UPDATE ranking_classes_8 SET scroe = %s, ranking = %s WHERE class = %s',
        (scroe, ranking, class_)
    )
    conn.commit()

def update_9(class_, scroe, ranking):
    _execute(
        'UPDATE ranking_classes_9 SET scroe = %s, ranking = %s WHERE class = %s',
        (scroe, ranking, class_)
    )
    conn.commit()

def find_scroe_7(class_):
    _execute(
        "SELECT * FROM ranking_classes_7 WHERE class = %s",
        (class_,)
    )
    result = cursor.fetchone()
    return result[1]

def find_scroe_8(class_):
    _execute(
        "SELECT * FROM ranking_classes_8 WHERE class = %s",
        (class_,)
    )
    result = cursor.fetchone()
    return result[1]

def find_scroe_9(class_):
    _execute(
        "SELECT * FROM ranking_classes_9 WHERE class = %s",
        (class_,)
    )
    result = cursor.fetchone()
    return result[1]

def find_ranking_7():
    _execute("SELECT * FROM ranking_classes_7")
    result = cursor.fetchall()
    return result, len(result)

def find_ranking_8():
    _execute("SELECT * FROM ranking_classes_8")
    result = cursor.fetchall()
    return result, len(result)

def find_ranking_9():
    _execute("SELECT * FROM ranking_classes_9")
    result = cursor.fetchall()
    return result, len(result)

def find_ranking_sporters(sport):
    _execute(
        "SELECT * FROM ranking_sporters WHERE sport = %s",
        (sport,)
    )
    result = cursor.fetchall()
    return result, len(result)

def clean_all():
    _execute('DELETE FROM people')
    _execute('DELETE FROM ranking_classes_7')
    _execute('DELETE FROM ranking_classes_8')
    _execute('DELETE FROM ranking_classes_9')
    _execute('DELETE FROM ranking_sporters')
    _execute('DELETE FROM sporter')
    _execute('DELETE FROM sports')
    _execute('INSERT INTO people (name, password, job) VALUES (%s, %s, %s)', ('1949', '1001', '总控'))
    _execute('INSERT INTO sports (sport) VALUES (%s)', (' ',))
    conn.commit()