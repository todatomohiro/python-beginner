"""
【Python】設定ファイルを作成・読み込みしてみよう！
configparserとyamlモジュールを使用して
configファイルの生成・読み込みを試してみます。

Blog URL : https://develop.blue/2020/02/python-use-config/
"""

print("\n-- configparserを使用 --")
print("\n設定ファイルの生成")
import configparser

config = configparser.ConfigParser()

config['BASE'] = {
    'aaaa': '1111111',
    'bbbb': '2222222'
}
config['TYPE'] = {
    'string': 'abcdefg',
    'number': 123456789,
    'bool': False
}
with open('sample/config.ini', 'w') as file:
    config.write(file)

print("\n設定ファイルの読み込み")
config = configparser.ConfigParser()
config.read('sample/config.ini')

print(config['BASE']['aaaa'])
print(config['TYPE']['number'])

# 下記の場合、値が存在しないためエラーが発生する
# print(config['BASE']['abc'])

# 下記の場合、値が存在しない場合Noneになる
read_base = config['BASE']
print(read_base.get('abc'))

print("\n-- YAMLを使用 --")
print("\n設定ファイルの生成")
import yaml

config = {
    'base': [
        'aaaa',
        'bbbb',
    ],
    'type': [
        'abcdefg'
    ]
}
with open('sample/config.yaml', 'w') as file:
    yaml.dump(config, file)

print("\n設定ファイルの読み込み")
with open('sample/config.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

    print(config['base'])
    print(config['type'])
