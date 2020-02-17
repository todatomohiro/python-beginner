print("\n-- 関数について --")
print("\nクロージャー")


def outer_function(x, y):
    def inner_function():
        return x + y

    return inner_function


outer = outer_function(1, 3)
print(outer())


def tax_price(tax_rate):
    def tax_calculation(price):
        return int(price + (tax_rate * 0.01) * price)

    return tax_calculation


tax_func = tax_price(10)

print(tax_func(100))
print(tax_func(200))

print("\nデコレータ")


def deco(func):
    def wrapper(*args, **kwargs):
        print('--start--')
        func(*args, **kwargs)
        print('--end--')

    return wrapper


@deco
def text_print(text):
    print(text)


text_print('abc')

print("\nラムダ")

lists = [1, 2, 3, 4]


def num_multiply(lists, func):
    for num in lists:
        print(func(num))


def multiply(num):
    return num * 10


num_multiply(lists, multiply)
num_multiply(lists, lambda num: num * 10)

print("\nジェネレーター")


def texts():
    yield 'aaa'
    yield 'bbb'
    yield 'ccc'


g = texts()
print(next(g))
print(next(g))
print(next(g))

print("\n-- 名前空間とスコープ --")
print("\nグローバル変数を関数内で参照")
text1 = 'abcde'


def func1():
    print(text1)


func1()
print(text1)

print("\nグローバル変数を関数内で変更(失敗)")
text2 = 'abcde'


def func2():
    text2 = 'ABCDE'
    print(text2)


func2()
print(text2)

print("\nグローバル変数を関数内で変更(成功)")
text3 = 'abcde'


def func3():
    global text3
    text3 = 'ABCDE'
    print(text3)


func3()
print(text3)
