#テンプレ―トをcity011として、未入力をcity012とするソースコード

import numpy as np

template_file_prefix = "city011/city011_"
template_data = []
template_framenum = []

uninput_file_prefix = "city012/city012_"
uninput_data = []
uninput_framenum = []

file_extension = ".txt"

#テンプレートデータの読み込み

for i in range(1, 101):
    file_path = template_file_prefix + str(i).zfill(3) + file_extension
    line_counter = 0 #行カウント
    file_data = []
    with open(file_path) as f: #テキストファイルを開く
        for line in f:
            line_counter += 1
            if line_counter < 4: #最初の数値に関係ない行をスキップ
                continue
            try:
                row = list(map(float, line.strip().split())) #一行ずつ書き込み
                file_data.append(row) #file_dataに一時的に格納
            except ValueError:
                continue
    if file_data: #file_dataが有効な時にtemplate_dataに追加
        template_data.append(file_data)
    #各単語のフレーム数
    template_framenum.append(line_counter - 3) #要素1：単語番号-1


# テンプレートデータを3次元配列に変換
template_data_3d = np.array(template_data) #要素1:単語番号-1　要素2:フレーム数-1　要素3:15次のメルケプストラム特徴量-1

#未入力データの読み込み
for i in range(1, 101):
    file_path = uninput_file_prefix + str(i).zfill(3) + file_extension
    line_counter = 0 #行カウント
    file_data = []
    with open(file_path) as f: #テキストファイルを開く
        for line in f:
            line_counter += 1
            if line_counter < 4: #最初の数値に関係ない行をスキップ
                continue
            try:
                row = list(map(float, line.strip().split())) #一行ずつ書き込み
                file_data.append(row) #file_dataに一時的に格納
            except ValueError:
                continue
    if file_data: #file_dataが有効な時にuninput_dataに追加
        uninput_data.append(file_data)
    #各単語のフレーム数
    uninput_framenum.append(line_counter - 3) #要素1：単語番号-1

# 未入力データを3次元配列に変換
uninput_data_3d = np.array(uninput_data) #要素1:単語番号-1　要素2:フレーム数-1　要素3:15次のメルケプストラム特徴量-1

#確認表示
print(template_data_3d[99][90][14])