"""
【Python】日付や時間を使ってみよう！
Pythonには日付や時間を扱うモジュールなど用意されています。
日付や時間に関する処理を確認します。

Blog URL : https://develop.blue/2020/02/python-use-datetime/
"""

print("\n現在の日時取得")
import datetime

now = datetime.datetime.now()
print(now)

print("\n現在の日時をフォーマット変更")
print(now.strftime('%Y/%m/%d %H:%M:%S'))

print("\n30分後の日時")
delta = datetime.timedelta(minutes=30)
print(now + delta)

print("\n1日前の日時")
delta = datetime.timedelta(days=1)
print(now - delta)
