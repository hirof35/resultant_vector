# ベクトル合力シミュレーター (Vector Resultant Simulator)

複数のベクトルを視覚的に合成し、その「合力」を2次元グラフ上に描画するPythonシミュレーターです。各ベクトルを原点から描画するだけでなく、ベクトルの「継ぎ足し（平行移動）」を点線で表現するため、合成のプロセスを直感的に理解することができます。
<img width="1918" height="1091" alt="スクリーンショット 2026-06-22 084234" src="https://github.com/user-attachments/assets/af98fba5-7d18-407f-b7a5-748438c45e08" />

## 機能・特徴
- 任意の本数・大きさのベクトル（X成分、Y成分）を自由に設定可能
- 複数のベクトルを「しりとり形式」で繋ぎ合わせた軌跡を点線で表示
- 全てのベクトルを足し合わせた最終的な「合力」を赤色の矢印で強調表示
- 入力されたベクトルの大きさに応じて、グラフの表示範囲（スケール）を自動調整

## 動作環境
- Python 3.8以上
- 必要なライブラリ: `matplotlib`, `numpy`

## セットアップ手順

1. **リポジトリのクローンまたはファイルの配置**
   プログラムファイル（`resultant_vector.py`）を任意のフォルダに配置します。

2. **仮想環境の作成と有効化（推奨）**
   ```bash
   python -m venv .venv
   # Windows (PowerShell) の場合:
   .\.venv\Scripts\Activate.ps1
   # Mac/Linux の場合:
   source .venv/bin/activate
必要なライブラリのインストール

Bash
pip install matplotlib numpy
※もし kiwisolver や _cext 関連のインポートエラーが発生した場合は、一度キャッシュをクリアして再インストールを試みてください：

Bash
pip install --force-reinstall --no-cache-dir matplotlib
使い方
resultant_vector.py を開き、冒頭にある vectors リスト内の数値を自由に書き換えます。

Python
vectors = [
    np.array([4, 2]),   # ベクトル1 [X成分, Y成分]
    np.array([-2, 5]),  # ベクトル2
    np.array([3, -3])   # ベクトル3
]
スクリプトを実行します。

Bash
python resultant_vector.py
実行するとMatplotlibのウィンドウが立ち上がり、青い矢印（各ベクトル）と赤い矢印（合力）のグラフが表示されます。
