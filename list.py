print("\nリスト型の変数作成")
list1 = ['a', 'b', 'c']
print(list1)
print(type(list1))

print("\n指定インデックスの要素取得")
list2 = ['a', 'b', 'c']
print(list2[1])

print("\n指定インデックスの要素変更")
list3 = ['a', 'b', 'c']
list3[1] = 'z'
print(list3)

print("\n複数階層のリスト作成")
list4 = [['a', 'b', 'c'], ['d', 'e', 'f']]
print(list4)
print(type(list4))

print("\n-- リスト型のよく使う処理 --")

print("\n指定インデックスの範囲で要素取得")
list17 = ['a', 'b', 'c', 'd', 'e']
print(list17[1:3]) # 開始インデックス ~ 終了インデックスまで
print(list17[:3]) # 始め ~ 終了インデックスまで
print(list17[3:]) # 開始インデックス ~ 終了まで

print("\n指定要素のインデックスを取得")
list18 = ['a', 'b', 'c']
print(list18.index('c'))

print("\n指定要素の数を取得")
list19 = ('a', 'b', 'c', 'a', 'd')
print(list19.count('a'))
print(list19.count('z'))

print("\n最終行に要素を追加")
list5 = ['a', 'b', 'c']
list5.append('z')
print(list)

print("\n指定インデックスの前に要素を追加")
list6 = ['a', 'b', 'c']
list6.insert(0, 'z')
print(list)

print("\n最後の要素を抜き出し")
list7 = ['a', 'b', 'c']
txt7 = list7.pop()  # 最終の要素を抜き出し
print(txt7)
print(list7)

print("\n指定インデックスの要素を抜き出し")
list8 = ['a', 'b', 'c']
txt8 = list8.pop(1)  # 1番の要素を抜き出し
print(txt8)
print(list8)

print("\n指定要素のインデックスを検索・取得")
list9 = ['a', 'b', 'c']
print(list9.index('b'))  # bの要素を抜き出し

print("\n指定要素を削除")
list10 = ['a', 'b', 'c', 'b']
list10.remove('b')  # bの要素を削除
print(list10)

print("\n指定インデックスの要素を削除")
list11 = ['a', 'b', 'c']
del list11[1]  # 1番キーの要素削除
print(list11)

print("\n指定インデックスの要素を削除")
list12 = ['a', 'b', 'c']
list12.clear()  # 全要素削除
print(list12)

print("\nリストの結合(extend)")
list13a = ['a', 'b', 'c']
list13b = ['d', 'e', 'f']
list13a.extend(list13b)  # extendにて配列を結合
print(list13a)
print(list13b)

print("\nリストの結合(+=)")
list14a = ['a', 'b', 'c']
list14b = ['d', 'e', 'f']
list14a += list14b  # +=にて配列を結合
print(list14a)
print(list14b)

print("\nリストの値を昇順並び替え")
list15 = ['5', '3', '1', '2', '4']
list15.sort()
print(list15)

print("\nリストの値を降順並び替え")
list16 = ['5', '3', '1', '2', '4']
list16.sort(reverse=True)
print(list16)
