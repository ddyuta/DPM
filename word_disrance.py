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
    with open(file_path) as f:
        for line in f:
            line_counter += 1
            if line_counter < 4:  # 最初の数値に関係ない行をスキップ
                continue
            try:
                row = list(map(float, line.strip().split()))
                file_data.append(row)
            except ValueError:
                continue
    if file_data:
        template_data.append(file_data)
    template_framenum.append(line_counter - 3)

# テンプレートデータを3次元配列に変換
template_data_3d = np.array(template_data)

# 未入力データの読み込み
for i in range(1, 101):
    file_path = uninput_file_prefix + str(i).zfill(3) + file_extension
    line_counter = 0  # 行カウント
    file_data = []
    with open(file_path) as f:
        for line in f:
            line_counter += 1
            if line_counter < 4:  # 最初の数値に関係ない行をスキップ
                continue
            try:
                row = list(map(float, line.strip().split()))
                file_data.append(row)
            except ValueError:
                continue
    if file_data:
        uninput_data.append(file_data)
    uninput_framenum.append(line_counter - 3)

# 未入力データを3次元配列に変換
uninput_data_3d = np.array(uninput_data)

# 行数を揃えて局所距離を計算
distances = np.zeros((100, 100))

for p in range(100):
    for q in range(100):
        template_data_3d_frame = np.array(template_data_3d[p])
        uninput_data_3d_frame = np.array(uninput_data_3d[q])
        template_framenum_frame = template_framenum[p]
        uninput_framenum_frame = uninput_framenum[q]

        diff = abs(template_framenum_frame - uninput_framenum_frame)

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


        local_distance = np.linalg.norm(template_data_3d_frame - uninput_data_3d_frame)
        distances[p][q] = local_distance

#確認表示
for n in range(100):
    print(distances[99][n])

print(distances[99][0])