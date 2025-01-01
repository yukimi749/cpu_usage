# cpu_usage
![test](https://github.com/yukimi749/cpu_usage/actions/workflows/test.yml/badge.svg)

CPUの使用率をトピックから出力する

## ディレクトリ構成
```
cpu_usage
├── LICENSE
├── README.md
├── cpu_usage
│   ├── __init__.py
│   └── cpu_utilization.py
├── launch
│   └── utilization.launch.py
├── package.xml
├── resource
│   └── cpu_usage
├── setup.cfg
├── setup.py
└── test
    ├── test.bash
    ├── test_copyright.py
    ├── test_flake8.py
    └── test_pep257.py
```
### ノード
`/cpu_utilization`

### トピック
`/cpu`

### テスト用ディレクトリ
`launch`  
`test`

## 使用方法
- psutilをインストールする  
`sudo apt install python3-pip`
`pip install psutil`

- リポジトリをクローン
`cd ~/ros2_ws/src`  
`git clone https://github.com/yukimi749/robosys2024.git`

- ディレクトリに移動  
`cd cpu_usage/cpu_usage`

- 実行権限を追加  
`chmod +x cpu_utilization.py`

- 以下のコマンドで実行する  
`ros2 run cpu_usage cpu_utilization`

## 実行例
```
[INFO] [1735732643.020914561] [cpu_utilization]: cpu_usage: "0.0"
[INFO] [1735732644.023848833] [cpu_utilization]: cpu_usage: "0.10000000149011612"
[INFO] [1735732645.027048696] [cpu_utilization]: cpu_usage: "3.5999999046325684"
[INFO] [1735732646.030160955] [cpu_utilization]: cpu_usage: "0.0"
[INFO] [1735732647.034149017] [cpu_utilization]: cpu_usage: "0.0"
[INFO] [1735732648.038025267] [cpu_utilization]: cpu_usage: "0.0"
[INFO] [1735732649.041805381] [cpu_utilization]: cpu_usage: "0.0"
[INFO] [1735732650.045667432] [cpu_utilization]: cpu_usage: "0.20000000298023224"
[INFO] [1735732651.049538563] [cpu_utilization]: cpu_usage: "0.0"
```
## 必要なソフトウェア
- Python
  - テスト済みバージョン：3.7~3.10

## テスト環境
- Ubuntu 22.04.5 LTS
- ROS2 Humble

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- © 2024 Yukimi Miyahara
