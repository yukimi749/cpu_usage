# cpu_usage
![test](https://github.com/yukimi749/cpu_usage/actions/workflows/test.yml/badge.svg)

- ROS2のパッケージ
- CPUの使用率をトピックから出力する

## ノード
### cpu_utilization
- psutilライブラリを使用してCPUの使用率を取得し1秒ごとにトピックにパブリッシュする

### listener
- テスト用
- トピックからメッセージをサブスクライブする

## トピック
### cpu
- メッセージの型：Float32

## 使用方法
※ここではワーキングディレクトリを`ros2_ws`としています

- psutilをインストールする  
`sudo apt install python3-pip`  
`pip install psutil`

- リポジトリをクローン  
`cd ~/ros2_ws/src`  
`git clone https://github.com/yukimi749/robosys2024.git`  

- パッケージをビルド  
`cd ~/ros2_ws`  
`colcon build`  

### 実行方法  
２つの端末で実行
  - 端末1  
`ros2 run cpu_usage cpu_utilization`  
  - 端末2  
`ros2 run cpu_usage listener`  

### 実行結果
```
[INFO] [1736316792.790200517] [listener]: Listen: 0.100000%
[INFO] [1736316793.793221956] [listener]: Listen: 0.000000%
[INFO] [1736316794.795402437] [listener]: Listen: 0.000000%
[INFO] [1736316795.797564332] [listener]: Listen: 0.000000%
[INFO] [1736316796.799398471] [listener]: Listen: 0.100000%
[INFO] [1736316797.802095704] [listener]: Listen: 0.000000%
[INFO] [1736316798.803414406] [listener]: Listen: 0.300000%
[INFO] [1736316799.805267649] [listener]: Listen: 1.700000%
[INFO] [1736316800.808251560] [listener]: Listen: 4.200000%
[INFO] [1736316801.810335455] [listener]: Listen: 0.100000%
[INFO] [1736316802.813210739] [listener]: Listen: 0.100000%
```

## テスト環境
- Ubuntu 22.04.5 LTS
- ROS2 Humble

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- © 2024 Yukimi Miyahara
