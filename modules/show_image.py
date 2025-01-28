import numpy as np
import matplotlib.pyplot as plt


def show_image(data: dict):
    # 赤、緑、青の各チャネルを取得
    red_channel = data[:1024].reshape(32, 32)  # 赤チャネル
    green_channel = data[1024:2048].reshape(32, 32)  # 緑チャネル
    blue_channel = data[2048:].reshape(32, 32)  # 青チャネル

    # 各チャネルを結合して RGB 画像を作成
    image = np.stack([red_channel, green_channel, blue_channel], axis=-1)

    # 画像を表示
    plt.imshow(image)
    # plt.axis("off")  # 軸を非表示にする
    plt.show()  # ipynbでは書かずとも暗黙的に動作することもある
