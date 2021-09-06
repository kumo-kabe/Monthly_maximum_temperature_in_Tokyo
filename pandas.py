import pandas as pd
import numpy as np

# CSVファイルの読み込み(東京都の7月～10月の年別最高気温)
data_d = pd.read_csv('./csv/data.csv')

# 先頭3行のデータを表示
print(data_d.head(3))

print(data_d.index)  # インデックスの情報
len(data_d.index)  # インデックスの長さ

print(data_d.isnull())  # 欠損値(NaN)の場合はTrue

# 「Non-Null Count」という項目に各列の要素数が出力される。欠損値がある列は他の列と件数不一致
print(data_d.info())

# 列year, month, maximum_temperatureで欠損値を含む行を削除する
data_d.dropna(subset=['year', 'month', 'maximum_temperature'])

# dropna()を呼び出すだけでは元のデータは変更されない
# DataFrameを欠損値を含む行・列を削除したものに更新したい場合は、引数にinplace=Trueを指定するか、削除後にDataFrameに再代入する
# 新規のDataFrameを作成してそちらへ代入すれば、元のデータも残せる
data_d.dropna(subset=['year', 'month', 'maximum_temperature'], inplace=True)
print(data_d.info())

'''
# 列maximum_temperatureの欠損値を20で穴埋め
data_d['maximum_temperature'].fillna(20, inplace=True)
# 列maximum_temperatureの欠損値をmaximum_temperatureの平均値で穴埋め
data_d['maximum_temperature'].fillna(data_d['maximum_temperature'].mean())
# 列maximum_temperatureの欠損値をmaximum_temperatureの中央値で穴埋め
data_d['maximum_temperature'].fillna(data_d['maximum_temperature'].median())
# 列maximum_temperatureの欠損値をmaximum_temperatureの最頻値で穴埋め
data_d['maximum_temperature'].fillna(data_d['maximum_temperature'].mode())
'''
