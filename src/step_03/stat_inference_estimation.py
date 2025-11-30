from scipy import stats
import numpy as np
import seaborn as sns

# Irisデータを再読み込み
df = sns.load_dataset('iris')

# 標本データ（がくの長さ）
sample_data = df['sepal_length']
n = len(sample_data)             # 標本サイズ
sample_mean = np.mean(sample_data)  # 標本平均（点推定値）
sample_std = np.std(sample_data, ddof=1)  # 標本標準偏差 (不偏標準偏差)

print("--- 標本データの概要 ---")
print(f"標本サイズ (n): {n}")
print(f"標本平均 (点推定値): {sample_mean:.3f}")
print(f"不偏標準偏差 (s): {sample_std:.3f}")

confidence_level = 0.95
alpha = 1 - confidence_level

# scipy.stats.t.interval を使用して信頼区間を計算
# loc: 標本平均 (推定の中心)
# scale: 標準誤差 (SE = s / sqrt(n))
# df: 自由度 (n-1)

confidence_interval = stats.t.interval(
    confidence=confidence_level,
    df=n - 1,
    loc=sample_mean,
    scale=sample_std / np.sqrt(n)  # 標準誤差
)

print("\n--- 母平均の推定（95%信頼区間） ---")
print(f"信頼水準: {confidence_level * 100}%")
print(f"信頼区間: ({confidence_interval[0]:.3f}, {confidence_interval[1]:.3f})")
