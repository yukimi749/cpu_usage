# cpu_usage
![test](https://github.com/yukimi749/cpu_usage/actions/workflows/test.yml/badge.svg)

ROS2のパッケージ
- CPUの使用率をトピックから出力する

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
## ノード
### cpu_utilization
- psutilライブラリを使用して1秒ごとにCPUの使用率をトピックから出力する
- トピック:`cpu`
- 送信するデータの型：String

### listener
- テスト用

## 使用方法
- psutilをインストールする  
`sudo apt install python3-pip`  
`pip install psutil`

- リポジトリをクローン  
`cd ~/ros2_ws/src`  
`git clone https://github.com/yukimi749/robosys2024.git`

### 実行方法
- 実行方法1  
  - ２つの端末で実行  
端末1  
`ros2 run cpu_usage cpu_utilization`
端末2  
`ros2 run cpu_usage listener`  

- 実行方法2  
１つの端末で実行  
`ros2 launch cpu_usage utilization.launch.py`

### 実行例
- 実行結果1
```
[INFO] [1735894197.609492395] [listener]: Listen: cpu_usage: 0.0%
[INFO] [1735894198.612823728] [listener]: Listen: cpu_usage: 0.1%
[INFO] [1735894199.614363340] [listener]: Listen: cpu_usage: 0.2%
[INFO] [1735894200.616717244] [listener]: Listen: cpu_usage: 0.1%
[INFO] [1735894201.619407268] [listener]: Listen: cpu_usage: 0.1%
[INFO] [1735894202.621758034] [listener]: Listen: cpu_usage: 0.0%
[INFO] [1735894203.624013686] [listener]: Listen: cpu_usage: 0.1%
```

- 実行結果2
```
[listener-2] [INFO] [1735894979.473645049] [listener]: Listen: cpu_usage: 0.0%
[listener-2] [INFO] [1735894980.475382266] [listener]: Listen: cpu_usage: 0.2%
[listener-2] [INFO] [1735894981.477145923] [listener]: Listen: cpu_usage: 0.0%
[listener-2] [INFO] [1735894982.478906305] [listener]: Listen: cpu_usage: 0.1%
[listener-2] [INFO] [1735894983.481181751] [listener]: Listen: cpu_usage: 0.3%
[listener-2] [INFO] [1735894984.484011404] [listener]: Listen: cpu_usage: 0.2%
[listener-2] [INFO] [1735894985.486258713] [listener]: Listen: cpu_usage: 0.1%
```

## テスト環境
- Ubuntu 22.04.5 LTS
- ROS2 Foxy

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードの一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/slides_marp/robosys2024](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2024)
- © 2024 Yukimi Miyahara
