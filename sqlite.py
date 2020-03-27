"""
【Python】SQLiteを使って情報を保管してみよう！
PythonのSqliteモジュールを利用して情報の読み書きをおこないます。
SQLiteは別途インストールしてください。
プログラム下にはコメントアウトで with構文とインメモリの処理を記入しています。

モードを切り替えることで処理を変更できます。
mode: none, create, insert, select

Blog URL : https://develop.blue/2020/03/python-use-sqlite/
"""
import sqlite3
from contextlib import closing

mode = 'none';
db_connect = sqlite3.connect('sqlite_test.db')

if mode == 'create':
    # 新規テーブル生成
    db_curs = db_connect.cursor()
    sql = 'CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, name1 STRING, name2 STRING)'
    db_curs.execute(sql)
    db_connect.commit()

elif mode == 'insert':
    # テーブルに情報追加
    db_curs = db_connect.cursor()
    sql = 'INSERT INTO users(name1, name2) values ("OSAKA", "TARO")'
    db_curs.execute(sql)
    db_connect.commit()

elif mode == 'select':
    # テーブルから情報を取得
    db_curs = db_connect.cursor()
    sql = 'SELECT * FROM users'
    db_curs.execute(sql)

    print(db_curs.fetchall())

db_connect.close()

# withにてクローズ忘れを防止
# with closing(sqlite3.connect('sqlite_test.db')) as db_connect:
#     db_curs = db_connect.cursor()
#     sql = 'SELECT * FROM users'
#     db_curs.execute(sql)
#
#     print(db_curs.fetchall())

# メモリ上にSQLiteを実行
# with closing(sqlite3.connect(':memory:')) as db_connect:
#     db_curs = db_connect.cursor()
#     sql = 'CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, name1 STRING, name2 STRING)'
#     db_curs.execute(sql)
#     db_connect.commit()