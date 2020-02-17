print("\n-- 関数について --")

print("\n関数を定義")
def text_output():
    print('text print')

text_output()


print("\n関数を定義(戻り値あり)")
def text_return():
    return 'text return'

print(text_return())


print("\n関数を定義(引数あり)")
def input_output(text):
    print(text)

input_output('abc')
input_output('def')


print("\n関数で引数と戻り値の型指定")
def param_int(num: int) -> int:
    print(num)

param_int(123)


print("\n関数の引数にデフォルト値設定")
def param_def(num=0):
    print(num)

param_def(123)
param_def()


print("\n関数の引数にキーワード引数を使用")
def param_keyword(str1, str2):
    print('str1:' + str1 + ' str2:' + str2)

param_keyword('aaa', 'bbb')
param_keyword('bbb', 'aaa')  # 引数の順番が変われば出力も変わる
param_keyword(str2='bbb', str1='aaa')  # 引数名を指定することで順番が変わって出力は変わらない


print("\n複数の引数をargsでまとめる")
def param_args(*args):
    print(args)

param_args('aaa', 'bbb', 'ccc')


print("\n引数を辞書化する")
def param_dict(**dicts):
    print(dicts)

param_dict(str2='bbb', str1='aaa')


print("\n-- docstringについて --")
print("\n記述内容")
def docstrings_def(param1, param2):
    """この関数は引数で渡された氏名を出力します

    :param param1: str 氏名(姓)
    :param param2: str 氏名(名)
    :return: None
    """

    print(param1 + ' ' + param2)


docstrings_def('Osaka', 'Taro')

help(docstrings_def)
print(docstrings_def.__doc__)

