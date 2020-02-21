"""
【Python】クラスを使ってみよう！
Pythonでクラスの作り方に関して確認をするスクリプトになります。

Blog URL : https://develop.blue/2020/02/python-use-class/
"""

print("\n-- クラス --")
print("\nクラス生成")
class Item1(object):
    # コンストラクタ
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate * 0.01

    def tax_price(self, price):
        return int(price + price * self.tax_rate)

    # デストラクタ
    def __del__(self):
        self.tax_rate = 0
        print('tax end')


item = Item1(10)
print(item.tax_price(100))
del item


print("\nクラスの継承")
class Item2a(object):
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate * 0.01

    def tax_price(self, price):
        return int(price + price * self.tax_rate)

class Item2b(Item2a):
    def tax_price_total(self, price, count):
        return int(price + price * self.tax_rate) * count

item = Item2b(10)
print(item.tax_price(100))
print(item.tax_price_total(100, 5))
del item


print("\nクラスの書き換え")
class Item3a(object):
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate * 0.01

    def tax_price(self, price):
        return int(price + price * self.tax_rate)

class Item3b(Item3a):
    def tax_price(self, price):
        return price + price * self.tax_rate

item = Item3b(10)
print(item.tax_price(100))
del item


print("\nクラス変数")
class Item4(object):
    tax_rate = 0.1  # クラス変数

    def tax_price(self, price):
        return int(price + price * self.tax_rate)

item = Item4()
print(item.tax_price(100))
del item


print("\nクラスメソッドとスタティックメソッド")
class Item4(object):
    tax = 10

    def __init__(self):
        self.tax_rate = self.tax * 0.01

    # エラーが発生する
    # def get_tax(self):
    #    return self.tax

    @classmethod
    def get_tax(cls):
        return cls.tax

item = Item4()
print(item.get_tax())
del item

item = Item4
print(item.get_tax())
del item