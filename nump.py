"""
【Python】NumPyで効率的に計算処理をしてみよう！
Pythonのnumpyモジュールを利用して計算処理をおこないます。
numpyモジュールは標準では無いため pip install numpy コマンドで
インストール後にお試しください。

Blog URL : https://develop.blue/2020/04/python-use-numpy/
"""

print("\n-- 基本メソッド --")
print("\nNumPyの配列を生成する")
import numpy

numpy_int = numpy.array([0, 1, 2, 3, 4, 5])
print(type(numpy_int))
print(numpy_int)

print("\nNumPyの型を統一")
numpy_float = numpy.array([0.2, 1.0, 1.8, 2.0, 3.3])
print(numpy_float)

numpy_str = numpy.array(['aa', 'bb', 'cc'])
print(numpy_str)

numpy_bool = numpy.array([True, False, False])
print(numpy_bool)

numpy_err = numpy.array([1, 'aa', False])
print(numpy_err)

print("\n容量を制限する")
numpy_int = numpy.array([0, 1, 2, 3, 4, 5], dtype=numpy.int8)
print(numpy_int)
print(numpy_int.dtype)

print("\nデータ型を変換する")
numpy_float = numpy.array([0.2, 1.0, 1.8, 2.0, 3.3])
print(numpy_float)

numpy_int = numpy_float.astype(numpy.int8)
print(numpy_int)

print("\n連続する整数を格納する")
numpy_int = numpy.arange(5)
print(numpy_int)

numpy_int = numpy.arange(5, 10)
print(numpy_int)

numpy_int = numpy.arange(5, 10, 2)
print(numpy_int)

print("\n引数条件で分割して格納する")
numpy_int = numpy.linspace(0, 10, 3)
print(numpy_int)

print("\n仮の値を指定数 格納する")
numpy_int = numpy.empty(5)
print(numpy_int)

print("\n数値0を指定数 格納する")
numpy_int = numpy.zeros(5)
print(numpy_int)

print("\nランダムな値を指定数 格納する")
numpy_float = numpy.random.rand(5)
print(numpy_float)

print("\nランダムな値を指定数 格納する")
numpy_int1 = numpy.array([1, 2, 3])
numpy_int2 = numpy.array([11, 22, 33])
numpy_int3 = numpy.concatenate([numpy_int1, numpy_int2])
print(numpy_int3)

print("\n多次元配列を生成する")
numpy_int = numpy.array([[0, 1, 2], [3, 4, 5]])
print(type(numpy_int))
print(numpy_int)

print("\n多次元配列を1次元配列に変換する")
numpy_int1 = numpy.array([[0, 1, 2], [3, 4, 5]])
numpy_int2 = numpy_int1.flatten()
print(numpy_int1)
print(numpy_int2)

print("\n1次元配列を多次元配列に変換する")
numpy_int1 = numpy.array([1, 2, 3, 4, 5, 6])
numpy_int2 = numpy_int1.reshape(3, 2)
print(numpy_int1)
print(numpy_int2)

print("\n-- NumPyの操作 --")
print("\n要素の参照(1次元配列)")
numpy_str = numpy.array(['a', 'b', 'c', 'd', 'e', 'f'])
print(numpy_str[0])
print(numpy_str[:3])
print(numpy_str[3:])
print(numpy_str[0:6:2])
print(numpy_str[::3])

print("\n要素の参照(多次元配列)")
numpy_str = numpy.array([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
print(numpy_str[0, 0])
print(numpy_str[:2, :1])
print(numpy_str[:2, :2])
print(numpy_str[1:3, 1:3])
print(numpy_str[0:3, 0:3:2])

print("\n要素の追加:append(1次元配列)")
numpy_str = numpy.array(['a', 'b', 'c'])
numpy_str = numpy.append(numpy_str, 'z')
print(numpy_str)

numpy_str = numpy.array(['a', 'b', 'c'])
numpy_str = numpy.append(numpy_str, ['x', 'y', 'z'])
print(numpy_str)

print("\n要素の追加:append(多次元配列)")
numpy_str = numpy.array([['a', 'b'], ['c', 'd']])
print(numpy_str)
numpy_str = numpy.append(numpy_str, [['x'], ['z']])
print(numpy_str)

print("\n要素の追加:insert(1次元配列)")
# IDX1番目に追加
numpy_str = numpy.array(['a', 'b', 'c'])
numpy_str = numpy.insert(numpy_str, 1, 'z')
print(numpy_str)

# IDX2番目に複数追加
numpy_str = numpy.array(['a', 'b', 'c'])
numpy_str = numpy.insert(numpy_str, 2, ['x', 'y', 'z'])
print(numpy_str)

print("\n要素の追加:insert(多次元配列)")
numpy_str1 = numpy.array([['a', 'b'], ['c', 'd']])
numpy_str2 = numpy.array(['x', 'y'])
# 最初の行に追加
numpy_str = numpy.insert(numpy_str1, 0, numpy_str2, 0)
print(numpy_str)

# IDX1行目に追加
numpy_str = numpy.insert(numpy_str1, 1, numpy_str2, 0)
print(numpy_str)

# IDX1列目に追加
numpy_str = numpy.insert(numpy_str1, 1, numpy_str2, 1)
print(numpy_str)

# 最終行に追加
(mh, mw) = numpy_str.shape
numpy_str = numpy.insert(numpy_str1, mh, numpy_str2, 0)
print(numpy_str)

# 最終列に追加
(mh, mw) = numpy_str.shape
numpy_str = numpy.insert(numpy_str1, mw, numpy_str2, 1)
print(numpy_str)

print("\n要素の削除:delete(1次元配列)")
# IDX1番目を削除
numpy_str = numpy.array(['a', 'b', 'c', 'd'])
numpy_str = numpy.delete(numpy_str, [1, 2])
print(numpy_str)

# IDX1と3番目を削除
numpy_str = numpy.array(['a', 'b', 'c', 'd'])
numpy_str = numpy.delete(numpy_str, [1, 3])
print(numpy_str)

print("\n要素の削除:delete(多次元配列)")
# IDX1行目を削除
numpy_str = numpy.array([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
numpy_str = numpy.delete(numpy_str, 1, 0)
print(numpy_str)

# IDX1列目を削除
numpy_str = numpy.array([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
numpy_str = numpy.delete(numpy_str, 1, 1)
print(numpy_str)

print("\n要素に四則演算(1次元配列)")
numpy_int1 = numpy.array([1, 2, 3, 4, 5, 6])
numpy_int2 = numpy_int1 + 1
print(numpy_int1)
print(numpy_int2)

numpy_int1 = numpy.array([1, 2, 3, 4, 5, 6])
numpy_int2 = numpy_int1 * 2
print(numpy_int1)
print(numpy_int2)

print("\n要素に四則演算(多次元配列)")
numpy_int1 = numpy.array([[1, 2], [3, 4]])
numpy_int2 = numpy_int1 + 1
print(numpy_int1)
print(numpy_int2)

numpy_int1 = numpy.array([[1, 2], [3, 4]])
numpy_int2 = numpy_int1 * 2
print(numpy_int1)
print(numpy_int2)

print("\n-- ユニバーサル関数 --")
print("\n要素の加算")
numpy_int1 = numpy.array([1, 2, 3])
numpy_int2 = numpy.array([1, 1, 1])
numpy_int = numpy.add(numpy_int1, numpy_int2)
print(numpy_int)

print("\n要素の減算")
numpy_int1 = numpy.array([1, 2, 3])
numpy_int2 = numpy.array([1, 1, 1])
numpy_int = numpy.subtract(numpy_int1, numpy_int2)
print(numpy_int)

print("\n多次元配列の要素格納を左右反転")
numpy_int = numpy.array([[1, 2, 3], [4, 5, 6]])
numpy_int = numpy.fliplr(numpy_int)
print(numpy_int)

print("\n多次元配列の要素格納を上下反転")
numpy_int = numpy.array([[1, 2, 3], [4, 5, 6]])
numpy_int = numpy.flipud(numpy_int)
print(numpy_int)

print("\n多次元配列の要素格納を回転")
numpy_int = numpy.array([[1, 2], [3, 4]])
# 0度
numpy_int = numpy.rot90(numpy_int, 0)
print(numpy_int)

# 1: 反時計周り90度
numpy_int = numpy.rot90(numpy_int, 1)
print(numpy_int)

# 2: 時計周り90度
numpy_int = numpy.rot90(numpy_int, 2)
print(numpy_int)

# 3: 180度
numpy_int = numpy.rot90(numpy_int, 3)
print(numpy_int)