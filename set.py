print("\n-- set型の集合 --")
print("\nset型の集合を生成")
set1 = {'a', 'b', 'c'}
# or
set1 = set({'a', 'b', 'c'})

print(set1)
print(type(set1))

print("\n要素の一意化")
set5 = {'a', 'b', 'c', 'd', 'b', 'c'}
print(set5)

print("\n要素の追加")
set2 = {'a', 'b', 'c'}
set2.add('z')  # zの要素追加
print(set2)

print("\n要素の削除")
set3 = {'a', 'b', 'c'}
set3.remove('c')  # cの要素削除
print(set3)

print("\n要素を取得して削除 (ランダム)")
set4 = {'a', 'b', 'c'}
txt4 = set4.pop()
print(txt4)
print(set4)

print("\n-- frozenset型の集合 --")
print("\nfrozenset型の集合を生成")
set5 = frozenset({'a', 'b', 'c'})

print(set5)
print(type(set5))

print("\n要素の追加(例外エラー)")
set6 = frozenset({'a', 'b', 'c'})
# set6.add('z')  # zの要素追加
print(set6)

print("\n-- 集合演算について --")
print("\n和集合(|)")
set7a = {'a', 'b', 'c'}
set7b = {'c', 'd'}
print(set7a | set7b)

print("\n差集合(-)")
set8a = {'a', 'b', 'c'}
set8b = {'c', 'd'}
print(set8a - set8b)

print("\n積集合(&)")
set9a = {'a', 'b', 'c'}
set9b = {'c', 'd'}
print(set9a & set9b)

print("\n対称差(^)")
set10a = {'a', 'b', 'c'}
set10b = {'c', 'd'}
print(set10a ^ set10b)
