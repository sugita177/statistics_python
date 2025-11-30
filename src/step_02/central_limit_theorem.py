import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- 日本語フォント設定（成功した設定を再利用）---
plt.rcParams['font.family']\
    = ['Meiryo', 'MS Gothic', 'Yu Gothic', 'DejaVu Sans']
plt.rcParams['font.sans-serif']\
    = ['Meiryo', 'MS Gothic', 'Yu Gothic', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
# --------------------------------------------------------

# シミュレーションパラメータ
sample_sizes = [1, 5, 30]  # 標本サイズ n
n_simulations = 10000  # サンプリング回数

# プロット領域の設定
fig, axes = plt.subplots(1, 3, figsize=(12, 5))
fig.suptitle('中心極限定理のシミュレーション（一様分布からサンプリング）', fontsize=16)

# 一様分布 (0, 10) からのサンプリング
low, high = 0, 10

for i, n in enumerate(sample_sizes):
    # 標本平均を格納するリスト
    sample_means = []

    # 10000回サンプリングを繰り返す
    for _ in range(n_simulations):
        # 一様分布からn個のデータを抽出
        samples = np.random.uniform(low, high, n)
        # 標本平均を計算してリストに追加
        sample_means.append(np.mean(samples))

    # ヒストグラムで分布を可視化
    sns.histplot(sample_means, bins=30, kde=True, ax=axes[i], color='coral')
    axes[i].set_title(f'標本サイズ n = {n}')
    axes[i].set_xlabel('標本平均')
    axes[i].set_ylabel('度数')

plt.tight_layout(rect=(0, 0.03, 1, 0.95))  # タイトルが被らないように調整
plt.show()
