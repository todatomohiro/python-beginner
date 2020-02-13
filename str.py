from decimal import Decimal

print("\n文字列の作成 (1行)")
str1 = 'ABCDEFG'
# or
str1 = "ABCDEFG"
print(str1)
print(type(str1))

print("\n文字列の作成 (複数行)")
str2 = '''ABCD
EFGH'''
# or
str2 = """ABCD
EFGH"""
print(str2)
print(type(str2))

print("\n文字列の作成 (複数行 改行対策なし)")
str3 = """ # 最初に改行が入っている
ABCD
EFGH       # 最初に改行が入っている
"""
print(str3)

print("\n文字列の作成 (複数行 改行対策あり)")
str4 = """\
ABCD
EFGH\
"""
print(str4)

print("\n-- 文字列の簡単な処理 --")

print("\n文字結合")
print("Python" "3")
# or
print("Python" + "3")

print("\n文字結合(エラー)")
# print("Python" + 3)

print("\n文字列を繰り返し")
print("Python." * 2)

print("\n指定された範囲の文字取得")
str5 = "ABCDEFG"
print(str5[1])  # n番目の文字取得

str6 = "ABCDEFG"
print(str6[-1])  # マイナスの場合は後ろから取得

str7 = "ABCDEFG"
print(str7[1:4])  # m番からn番まで指定範囲の文字取得

str8 = "ABCDEFG"
print(str8[:4])  # 0番からn番目まで指定範囲の文字取得

str9 = "ABCDEFG"
print(str9[4:])  # n番から最後まで指定範囲の文字取得

str10 = "ABCDEFG"
# print(str10[7])  # 範囲を超える文字取得はエラー

print("\n-- 文字代入 --")
print("\nformatを使って代入")
str11 = "ABC{}GHI"
print(str11.format("DEF"))

str12 = "AB{}EF{}IJ"
print(str12.format("CD", "GH"))  # 複数代入する事も可能

str13 = "AB{0}EF{1}IJ"
print(str13.format("CD", "GH"))  # 代入の順番を決めることも可能

str14 = "AB{1}EF{0}IJ"
print(str14.format("CD", "GH"))  # 代入の順番を決めることも可能

str15 = "AB{txt1}EF{txt2}IJ"
print(str15.format(txt1="CD", txt2="GH"))  # 代入にキー名を設定する事も可能

print("\nf-stringsを使って代入")
str16a = "CD"
str16b = "GH"
print(f"AB{str16a}EF{str16b}IJ")

print("\n%演算子を使って代入")
str17 = "CD"
print("AB%sEF" % (str17))
