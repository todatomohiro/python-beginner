from decimal import Decimal

print("\nint型 (整数)の作成")
num1 = int(5)
# or
num1 = 5
print(num1)
print(type(num1))

print("\nfloat型 (小数: 浮動小数点型) の作成")
num2 = float(5.1)
# or
num2 = 5.1
print(num2)
print(type(num2))

print("\ndecimal型 (小数: 固定小数点型) の作成1")
num3 = Decimal(5.1)  # 5.1は浮動小数点型
print(num3)
print(type(num3))

print("\ndecimal型 (小数: 固定小数点型) の作成2")
num4 = Decimal("5.1")  # 5.1は文字列型
print(num4)
print(type(num4))

print("\n-- 計算処理 --")
print(2 + 3)  # 加算
# 結果 5

print(5 - 1)  # 減算
# 結果 4

print(3 * 2)  # 乗算
# 結果 6

print(5 / 2)  # 除算
# 結果 2.5

print(5 % 2)  # 剰余
# 結果 1

print(5 // 2)  # 割り算の整数部のみ
# 結果 2

print(2 ** 3)  # べき乗 (例は2の3乗)
# 結果 8

print("\n-- 数値のキャスト(変換) --")
print("\nint型からfloat型へ変換")
num5 = int(5)
print(type(num5))  # 変換前は int型

num5 = float(num5)  # int型からfloat型へ変換

print(num5)
print(type(num5))  # 変換後は float型


print("\nfloat型からint型へ変換")
num6 = float(5.12)
print(type(num6))  # 変換前は float型

num6 = int(num6)  # float型からint型へ変換

print(num6)
print(type(num6))  # 変換後は int型
