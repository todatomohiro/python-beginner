print("\n辞書型を作成")
dict1 = {'l': 10, 'm': 20, 'n': 30}
# or
dict1 = dict(l=10, m=20, n=30)
print(dict1)
print(type(dict1))

print("\n指定キーの要素取得")
dict2 = {'l': 10, 'm': 20, 'n': 30}
print(dict2['m'])  # mキーの値取得

print("\n指定キーの要素変更")
dict3 = {'l': 10, 'm': 20, 'n': 30}
dict3['m'] = 99  # mキーの値変更
print(dict3)

print("\n指定キーの要素削除")
dict4 = {'l': 10, 'm': 20, 'n': 30}
del dict4['m']  # mキーの値削除
print(dict4)

print("\n-- 辞書型のよく使う処理 --")
print("\n指定キーの要素取得(例外対応)")
dict5 = {'l': 10, 'm': 20, 'n': 30}
# print(dict5['z'])  # 存在しないzキーの値取得

dict6 = {'l': 10, 'm': 20, 'n': 30}
print(dict6.get('z'))  # 存在しないzキーの値取得
print(dict6.get('z', 0))  # 存在しないzキーの値取得(デフォルト:0)

print("\n繰り返し処理(for)を使ったキー:要素の取得")
dict7 = {'l': '10', 'm': '20', 'n': '30'}
for key, num in dict7.items():
    print(key + ':' + num)

print("\n繰り返し処理(for)を使ったキーの取得")
dict8 = {'l': '10', 'm': '20', 'n': '30'}
for key in dict8.keys():
    print(key)

print("\n繰り返し処理(for)を使った要素の取得")
dict9 = {'l': '10', 'm': '20', 'n': '30'}
for num in dict9.values():
    print(num)