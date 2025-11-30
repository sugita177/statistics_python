from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# --- 日本語フォント設定（成功した設定を再利用）---
plt.rcParams['font.family']\
    = ['Meiryo', 'MS Gothic', 'Yu Gothic', 'DejaVu Sans']
plt.rcParams['font.sans-serif']\
    = ['Meiryo', 'MS Gothic', 'Yu Gothic', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
# --------------------------------------------------------

# 正規分布のパラメータを設定
mu = 50     # 平均
sigma = 10  # 標準偏差

# X軸の範囲を定義 (平均から±4標準偏差の範囲)
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 100)

# 確率密度関数 (PDF) の値を計算
pdf = norm.pdf(x, loc=mu, scale=sigma)

# プロット
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, color='blue', label=f'N(μ={mu}, σ={sigma})')
plt.title('正規分布の確率密度関数')
plt.xlabel('X')
plt.ylabel('確率密度')
plt.fill_between(x, pdf, color='skyblue', alpha=0.3)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
