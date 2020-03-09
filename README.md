一、介绍
=======
1.读取写入本地CSV格式的rmbData文件

2.根据数据生成柱状图\线性图,查看NS点卡价格走势

3.查看各个类型的点卡 对应rmb的比值,得到最合算的选择

二、使用
=======
依赖库
-----
```javascript
pip install pandas numpy matplotlib
```

运行
----
```javascript
python3 spider.py
```

交互界面解释
----------
i ----input 向CSV文件写入数据, 数据可以通过 空格 分割,会自动转化为CSV格式
p ----picture 查看图象
q ----quit 退出程序