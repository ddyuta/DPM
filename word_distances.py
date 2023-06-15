#テンプレートをcity011として未入力をcity012とするDPMソースコード

import numpy as np
import random

template_file_prefix = "city011/city011_"
template_data = []
template_framenum = []

uninput_file_prefix = "city012/city012_"
uninput_data = []
uninput_framenum = []

file_extension = ".txt"

# テンプレートデータの読み込み
for i in range(1, 101):
    file_path = template_file_prefix + str(i).zfill(3) + file_extension
    line_counter = 0  # 行カウント
    file_data = []
    with open(file_path) as f: # テキストファイルを開く
        for line in f:
            line_counter += 1
            if line_counter < 4:  # 最初の数値に関係ない行をスキップ
                continue
            try:
                row = list(map(float, line.strip().split())) # 一行ずつ書き込む
                file_data.append(row) # file_dataに一時的に格納
            except ValueError:
                continue
    if file_data: # file_dataが有効な時にappendを用いてテキストファイルのデータをそのまま二次元配列として
        template_data.append(file_data)

    # 各単語のフレーム数を1次元配列として
    # x=0,1番目のフレーム数‥x=99,100番目のフレーム数
    template_framenum.append(line_counter - 3) 

# テンプレートデータを3次元配列に変換
# deps = 単語番号-1, rows = 行-1, column = 列-1
template_data_3d = np.array(template_data)

# 未入力データの読み込み
for i in range(1, 101):
    file_path = uninput_file_prefix + str(i).zfill(3) + file_extension
    line_counter = 0  # 行カウント
    file_data = []
    with open(file_path) as f: #テキストファイルを開く
        for line in f:
            line_counter += 1
            if line_counter < 4:  # 最初の数値に関係ない行をスキップ
                continue
            try:
                row = list(map(float, line.strip().split())) # 一行ずつ書き込む
                file_data.append(row) # file_dataに一時的に格納
            except ValueError:
                continue
    if file_data: # file_dataが有効な時にappendを用いてテキストファイルのデータをそのまま二次元配列として
        uninput_data.append(file_data)

    # 各単語のフレーム数を1次元配列として
    # x=0,1番目のフレーム数‥x=99,100番目のフレーム数
    uninput_framenum.append(line_counter - 3)

# 未入力データを3次元配列に変換
# deps = 単語番号-1, rows = 行-1, column = 列-1
uninput_data_3d = np.array(uninput_data)

# 行数を揃えて局所距離を計算
distances = np.zeros((100, 100))

# フレーム数を調整する
for p in range(100):
    for q in range(100):
        template_data_3d_frame = np.array(template_data_3d[p])
        uninput_data_3d_frame = np.array(uninput_data_3d[q])
        template_framenum_frame = template_framenum[p]
        uninput_framenum_frame = uninput_framenum[q]

        # フレーム数の差をdiffとする
        diff = abs(template_framenum_frame - uninput_framenum_frame)

        # テンプレ―トと未入力のフレームの大小を比較し、フレーム数が大きいデータの数の差分をランダムで行を削除する

        if template_framenum_frame < uninput_framenum_frame:
            random_numbers = random.sample(range(uninput_framenum_frame), diff)
            uninput_data_3d_frame = np.delete(uninput_data_3d_frame, random_numbers, axis=0)
            for d in range(diff):
                uninput_framenum_frame -= 1
        elif template_framenum_frame > uninput_framenum_frame:
            random_numbers = random.sample(range(template_framenum_frame), diff)
            template_data_3d_frame = np.delete(template_data_3d_frame, random_numbers, axis=0)
            for d in range(diff):
                template_framenum_frame -= 1

        # ノルムを用いてテンプレートデータと未入力データのベクトルを計算
        local_distance = np.linalg.norm(template_data_3d_frame - uninput_data_3d_frame)
        # row : テンプレートデータの単語番号 column : 未入力データの単語番号
        # 例 : distances[row][colimn]で(ros-1)番目のテンプレートデータと(column-1)番目の未入力データの局所距離
        distances[p][q] = local_distance

#各単語の最小距離を知りたいとき
for p in range(100):
    min_distance = float('inf') # 初期値として無限大を設定
    for q in range(100):
        if distances[p][q] < min_distance:
            min_distance = distances[p][q]
    print(p, min_distance)

#ピンポイントで距離を知りたいとき
#print(distances[99][99])

#テンプレートの単語番号を固定して未入力１～１００までの距離を知りたいとき
#for n in range(100):
#    print(distances[99][n])
