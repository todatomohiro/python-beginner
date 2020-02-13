print("\nタプル型の変数作成")
tuple1 = ('a', 'b', 'c')
print(tuple1)
print(type(tuple1))

print("\n指定キーの要素取得")
tuple2 = ('a', 'b', 'c')
print(tuple2[1])

print("\n指定キーの要素変更 (NG)")
tuple3 = ('a', 'b', 'c')
# tuple3[1] = 'Z'
print(tuple3)

print("\n指定インデックスの範囲で要素取得")
tuple4 = ('a', 'b', 'c', 'd', 'e')
print(tuple4[1:3]) # 開始インデックス ~ 終了インデックスまで
print(tuple4[:3]) # 始め ~ 終了インデックスまで
print(tuple4[3:]) # 開始インデックス ~ 終了まで

print("\n指定要素のインデックスを取得")
tuple5 = ('a', 'b', 'c')
print(tuple5.index('c'))

print("\n指定要素の数を取得")
tuple6 = ('a', 'b', 'c', 'a', 'd')
print(tuple6.count('a'))
print(tuple6.count('z'))