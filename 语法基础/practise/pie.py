import pyecharts.options as opts
from pyecharts.charts import Pie

def draw_pie():    
    x_data = ["直接访问", "邮件营销", "联盟广告", "视频广告", "搜索引擎"]
    y_data = [335, 310, 274, 235, 400]
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
                title="Customized Pie",
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
    draw_pie()