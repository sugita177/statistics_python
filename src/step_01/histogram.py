import matplotlib.pyplot as plt
import seaborn as sns


# --- 日本語フォント設定（成功した設定を再利用）---
plt.rcParams['font.family']\
    = ['Meiryo', 'MS Gothic', 'Yu Gothic', 'DejaVu Sans']
plt.rcParams['font.sans-serif']\
    = ['Meiryo', 'MS Gothic', 'Yu Gothic', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
# --------------------------------------------------------

# seabornに内蔵されているIrisデータセットを読み込む
df = sns.load_dataset('iris')

# 最初の5行を表示してデータ構造を確認
print("\n--- データの先頭5行 ---")
print(df.head())

# データフレームの基本情報（欠損値、データ型など）を確認
print("\n--- データ情報 ---")
df.info()

print("\n--- 全体の要約統計量 (describe) ---")
print(df.describe())

# 'sepal_length'（がくの長さ）の平均値と中央値
mean_len = df['sepal_length'].mean()
median_len = df['sepal_length'].median()

# 'sepal_length'の標本分散と標準偏差（pandasはデフォルトで標本分散を計算）
variance_len = df['sepal_length'].var()
std_dev_len = df['sepal_length'].std()

# 相関係数行列の計算（変数間の線形な関係の強さを把握）
correlation_matrix = df.drop('species', axis=1).corr()  # 'species'列を除外して計算

print(f"\n- がくの長さの平均値: {mean_len:.2f}")
print(f"- がくの長さの中央値: {median_len:.2f}")
print(f"- がくの長さの分散: {variance_len!r:.2f}")
print(f"- がくの長さの標準偏差: {std_dev_len:.2f}")
print("\n--- 相関係数行列 ---")
print(correlation_matrix)

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='sepal_length', kde=True, bins=15)
plt.title('がくの長さのヒストグラム')
plt.xlabel('がくの長さ (cm)')
plt.ylabel('度数')
plt.grid(axis='y', alpha=0.5)
plt.show()
