# fund_sharp

* 这是一个基金夏普比率查询工具

* 输入: 基金代码

* 输出: 最新规模(scale), 最大回撤(withdrawal), 夏普比率(sharp), 波动率(volatility), 基金代码(code)

## 输入示例

```shell
python fund_sharp.py 110027
```

## 输出示例

```json
{"code": "110027", "sharp": "0.96", "volatility": "12.31", "scale": "119.35\u4ebf", "withdrawal": "15.38"}
```

## 说明

* 测试环境为Python 2.7
* 执行过程中会提示 "PhantomJS has been deprecated", 请忽略.
* 基金代码仅为6位数字, 不可少于6位或包含字母.
* 如果显示找不到 bs4 模块请自行安装 pip3 install beautifulsoup4 ,依然不行则手动下载到python2.7 根目录并 python setp.py install 安装

* Python3.8 环境
* 如果报错，请检查是否已经安装以下模块,若不全,请手动安装
* pip install beautifulsoup4
* pip install selenium
* pip install --upgrade numpy



