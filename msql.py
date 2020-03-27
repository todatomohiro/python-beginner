"""
【Python】MySQLを使って情報を保管してみよう！
サードパーティーのmysql-connector-pythonモジュールを利用して情報の読み書きをおこないます。
MySQLは別途インストールしてください。

モードを切り替えることで処理を変更できます。
mode: none, create, insert, update, delete, select

Blog URL : https://develop.blue/2020/03/python-use-mysql/
"""
import mysql.connector

mode = 'none'
db_connect = mysql.connector.connect(
    host='172.0.0.1',
    port='3306',
    user='root',
    password='root',
    database='mysql_test',
)

if mode == 'create':
    # 新規テーブル生成
    db_curs = db_connect.cursor()
    sql = 'CREATE TABLE users(id int NOT NULL AUTO_INCREMENT, name1 varchar(20), name2  varchar(20), PRIMARY KEY (id))'
    db_curs.execute(sql)
    db_connect.commit()

elif mode == 'insert':
    # テーブルに情報追加
    db_curs = db_connect.cursor()
    sql = 'INSERT INTO users(name1, name2) values ("OSAKA", "TARO")'
    db_curs.execute(sql)
    db_connect.commit()

elif mode == 'update':
    # テーブルの情報を変更
    db_curs = db_connect.cursor()
    sql = 'UPDATE users SET name2="ZIROU" WHERE id = 1'
    db_curs.execute(sql)
    db_connect.commit()

elif mode == 'delete':
    # テーブルの情報を削除
    db_curs = db_connect.cursor()
    sql = 'DELETE FROM users WHERE id = 1'
    db_curs.execute(sql)
    db_connect.commit()

elif mode == 'select':
    # テーブルから情報を取得
    db_curs = db_connect.cursor()
    sql = 'SELECT * FROM users'
    db_curs.execute(sql)

    print(db_curs.fetchall())

db_connect.close()
