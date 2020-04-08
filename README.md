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