from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
# 内置主题类型可查看 pyecharts.globals.ThemeType
# 有LIGHT DARK WHITE CHALK ESSOS INFOGRAPHIC
# VINTAGE WALDEN WESTROS WONDERLAND等十余种

# 第一幅图， 数据固定
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
    .add_xaxis(['LoL', 'QQ飞车', 'QQ炫舞', 'CF', 'DNF'])
    .add_yaxis('中国', [1000000, 300000, 200000, 600000, 800000])
    .add_yaxis('外国', [800000, 350000, 450000, 650000, 254000])
    .set_global_opts(title_opts=opts.TitleOpts(title='网游人气对比'))
)
bar.render(path='网游人气对比.html')

# 第二幅图，数据分离
items = ['Huawei', 'Vivo', 'Oppo', 'Xiaomi', 'Apple', 'Others']
data_list1 = [5180, 4690, 3120, 3300, 4690, 12460]
data_list2 = [6670, 3950, 2940, 3230, 4560, 11410]
bar1 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    .add_xaxis(items)
    .add_yaxis("2018年", data_list1)
    .add_yaxis("2019年", data_list2)
    .set_global_opts(title_opts=opts.TitleOpts(title='手机销售量对比/单位（万）', subtitle='2018-2019'))
)
bar1.render(path="手机销售量对比.html")