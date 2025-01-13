from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
lst1=[['泽慧',20],['子雯',20],['大米',20]]
c = (
    Pie()
    #.add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .add("",lst1)
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-设置颜色"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_set_color.html")
)
# for z in zip(Faker.choose(), Faker.values()):
#     print(z)

