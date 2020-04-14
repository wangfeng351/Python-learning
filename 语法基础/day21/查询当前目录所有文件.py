"""
查找当前目录所有文件
@Date 2020.04.14
"""
import pyecharts.options as opts
from pyecharts.charts import Pie
import os


text = 0
json = 0
html = 0
jpg = 0
csv = 0
def get_all(cwd):
    result = []
    # 遍历当前目录，获取文件列表，自己调试看各自步骤的结果
    get_dir = os.listdir(cwd)
    # print(get_dir)
    index = 1
    for i in get_dir:
        # 把第一个获取的文件夹加入路径，自己调试看各个的步骤的结果
        # print(i)
        sub_dir = os.path.join(cwd, i)
        # print(sub_dir)
        # 如果当前仍然是文件夹，递归调用
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            # 如果当前路径不是文件夹，则把文件名放入列表
            file_name = os.path.basename(sub_dir)
            if file_name.split(".")[-1] == "text":
                global text
                text += 1
            if file_name.split(".")[-1] == "json":
                global json
                json += 1
            if file_name.split(".")[-1] == "html":
                global html
                html += 1
            if file_name.split(".")[-1] == "jpg":
                global jpg
                jpg += 1
            if file_name.split(".")[-1] == "csv":
                global csv
                csv += 1
            result.append(file_name)
    return result


def draw_pie():
    x_data = ['text', 'json', 'html', 'jpg', 'csv']
    y_data = [text, json, html, jpg, csv]
    data_pair = [list(z) for z in zip(x_data, y_data)]
    data_pair.sort(key=lambda x: x[1])
    (
        Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
        .add(
            series_name="访问来源",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="各类文件数量统计",
                pos_left="center",
                pos_top="20",
                title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
        )
        .render("customized_pie.html")
    )

if __name__ == "__main__":
    # 取得当前目录：
    cur_path = os.getcwd() + "/语法基础"
    # print(cur_path)
    # 调用函数，同级语法基础目录下的文件
    # get_all(cur_path)
    get_all(cur_path)
    draw_pie()
