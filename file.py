"""
【Python】ファイル操作をしてみよう！
Pythonにはテキストの作成・追記等を行う機能や
圧縮ファイルにまとめるモジュールなどを確認します。

Blog URL : https://develop.blue/2020/02/python-use-file/
"""

print("\n-- テキストファイル --")
print("\n書き込み")
fp = open('sample/file.txt', 'w')
fp.write('test1\n')
fp.write('test2\n')
fp.close()

print("\n追記")
fp = open('sample/file.txt', 'a')
fp.write('test3\n')
fp.close()

print("\n読み込み")
fp = open('sample/file.txt', 'r')
print(fp.read())
fp.close()

print("\n行単位で処理をする")
fp = open('sample/file.txt', 'r')
while True:
    line = fp.readline()
    if (not line):
        break
    print(line, end='')
fp.close()

print("\n書き込み後に読み込み")
fp = open('sample/file.txt', 'w+')
fp.write('test\n')
fp.seek(0)  # ポインタを0文字目に戻す
print(fp.read())
fp.close()

print("\n-- CSVファイル --")
print("\n書き込み")
import csv

with open('sample/file.csv', 'w') as fp:
    # レコード変数定義
    fields = ['Name', 'Age']
    writer = csv.DictWriter(fp, fieldnames=fields)

    # ヘッダー書き込み
    writer.writeheader()

    # レコード書き込み
    writer.writerow({'Name': 'AAA', 'Age': '21'})
    writer.writerow({'Name': 'BBB', 'Age': '25'})

print("\n追記")
import csv

with open('sample/file.csv', 'a') as fp:
    # レコード変数定義
    fields = ['Name', 'Age']
    writer = csv.DictWriter(fp, fieldnames=fields)

    # レコード書き込み
    writer.writerow({'Name': 'CCC', 'Age': '30'})

print("\n読み込み")
with open('sample/file.csv', 'r') as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        print(row['Name'] + ':' + row['Age'])

print("\n-- ファイル圧縮 --")
print("\nTARGZで圧縮")
import tarfile

with tarfile.open('sample/file.tar.gz', 'w:gz') as fp:
    fp.add('sample')

print("\nTARGZの解凍")
with tarfile.open('sample/file.tar.gz', 'r:gz') as fp:
    fp.extractall('targz')

print("\nZIPで圧縮")
import zipfile

with zipfile.ZipFile('sample/file.zip', 'w') as fp:
    fp.write('sample')
    fp.write('sample/file.txt')

print("\nZIPの解凍")
with zipfile.ZipFile('sample/file.zip', 'r') as fp:
    fp.extractall('zip')

print("\n-- 一時ファイル(TMP) --")
print("\n一時ファイルの使用")
import tempfile

with tempfile.NamedTemporaryFile(delete=False) as tp:
    with open(tp.name, 'w+') as fp:
        fp.write('test\n')
        fp.seek(0)  # ポインタを0文字目に戻す
        print(fp.read())

print(tp.name)  # 添付ファイル位置

print("\nwithを使用してクローズ忘れ防止")
with open('sample/file.txt', 'r') as fp:
    print(fp.read())
