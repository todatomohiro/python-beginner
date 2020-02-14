print("\nif文 (真のみ)")
tmp = 'AAA'
if tmp == 'AAA':
    print('内容はAAAです')

print("\nif文 (真偽)")
if tmp == 'BBB':
    print('内容はBBBです')
else:
    print('内容はその他です')

print("\nif文 (条件式を2つ以上)")
if tmp == 'BBB':
    print('内容はBBBです')
elif tmp == 'AAA':
    print('内容はAAAです')
else:
    print('内容はその他です')

print("\nwhile文")
num = 0
while num < 4:
    num += 1
    print(num)

print("\nwhile文 (break使用)")
num = 0
while num < 4:
    num += 1
    if num == 2:
        break
    print(num)

print("\nwhile文 (continue使用)")
num = 0
while num < 4:
    num += 1
    if num == 2:
        continue
    print(num)

print("\nfor文 (リスト使用)")
array = ['a', 'b', 'c']
for key in array:
    print(key)

print("\nfor文 (文字列使用)")
str1 = 'abc'
for key in str1:
    print(key)

print("\nfor文 (辞書型使用)")
array = {'a': '100', 'b': '200', 'c': '300'}
for key, value in array.items():
    print(key + ' : ' + value)

print("\nfor文 (break使用)")
array = ['a', 'b', 'c']
for key in array:
    if key == 'b':
        break
    print(key)

print("\nfor文 (continue使用)")
array = ['a', 'b', 'c']
for key in array:
    if key == 'b':
        continue
    print(key)

print("\nfor文 (zip関数を使い複数配列処理)")
array1 = ['a', 'b', 'c']
array2 = ['1', '2', '3']
for str1, str2 in zip(array1, array2):
    print(str1 + ' : ' + str2)
