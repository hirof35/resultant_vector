import matplotlib.pyplot as plt
import numpy as np

# 1. 入力ベクトルを定義 [x成分, y成分]
# 好きなだけベクトルを追加・変更できます
vectors = [
    np.array([4, 2]),   # ベクトルA
    np.array([-2, 5]),  # ベクトルB
    np.array([3, -3])   # ベクトルC
]

# 2. 合力（全てのベクトルの和）を計算
resultant_vector = sum(vectors)

# 3. グラフのプロット設定
fig, ax = plt.subplots(figsize=(8, 8))
ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
ax.axhline(0, color='black', linewidth=1.2) # X軸
ax.axvline(0, color='black', linewidth=1.2) # Y軸

# 4. 各ベクトルを「始点を原点(0,0)」として描画
# ※合成のイメージが湧きやすいよう、薄い色で描画します
for i, v in enumerate(vectors):
    ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, 
              color='blue', alpha=0.4, label=f'Vector {i+1}: {v}' if i==0 else f'Vector {i+1}: {v}')

# 5. ベクトルを視覚的に「継ぎ足し（平行移動）」して合力を表現
origin = np.array([0, 0])
for v in vectors:
    ax.quiver(origin[0], origin[1], v[0], v[1], angles='xy', scale_units='xy', scale=1, 
              color='blue', alpha=0.7, linestyle=':')
    origin = origin + v # 次のベクトルの始点を更新

# 6. 合力ベクトル（始点から最終到達点まで）を赤色で描画
ax.quiver(0, 0, resultant_vector[0], resultant_vector[1], angles='xy', scale_units='xy', scale=1, 
          color='red', width=0.008, label=f'Resultant: {resultant_vector}')

# 7. グラフの表示範囲を自動調整
all_points = np.array([0, 0])
current = np.array([0, 0])
for v in vectors:
    current = current + v
    all_points = np.vstack([all_points, v, current])

max_val = np.max(np.abs(all_points)) + 2
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])

# 8. ラベルとタイトルの設定
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Vector Resultant Simulator')
ax.legend()
ax.set_aspect('equal') # 縦横比を1:1にする

# グラフを表示
plt.show()
