"""
使用pytcharts绘制仪表盘
@Date 2020.04.08
"""

from pyecharts import charts

# 仪表盘
gauge = charts.Gauge()
gauge.add('wf的Python小例子',[('Python机器学习', 30), ('Python基础', 70.), ('Python正则', 90)])
gauge.render(path="仪表盘.html")
print('ok')