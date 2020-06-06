"""
气泡图
@Date 2020.06.06
Seaborn是一种基于matplotlib的图形可视化python libraty
它提供了一种高度交互式界面，便于用户能够做出各种有吸引力的统计图表
pip install seaborn
"""
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import patches
import matplotlib.pyplot as plt

from scipy.spatial import ConvexHull
import warnings
warnings.simplefilter('ignore')

sns.set_style("white")


# Step 1 : Prepare Date
midwest = pd.read_csv(
    "./语法基础/res/csv/midwest_filter1.csv"
)

# As many colors as there are unique midwest['category']
categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i/float(len(categories)-1))
          for i in range(len(categories))]

# Step 2:Draw Scatterplot with unique color for each category
fig = plt.figure(figsize=(16, 10), dpi=80, facecolor="w", edgecolor="k")

for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal', data=midwest.loc[midwest.category ==
                                                     category, :], s='dot_size', c=colors[i], label=str(
        category), edgecolors='black', linewidths=.5)

# Step 3:Encircling


def encircle(x, y, ax=None, **kw):
    if not ax:
        ax = plt.gca()
    p = np.c_[x, y]
    hull = ConvexHull(p)
    poly = plt.Polygon(p[hull.vertices, :], **kw)
    ax.add_patch(poly)


# Select date to be encircled
midwest_encircle_data = midwest.loc[midwest.state == 'IN', :]

# Draw polygon surrounding vertices
encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal,
         ec="k", fc="gold", alpha=0.1)
encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal,
         ec="firebrick", fc="none", linewidth=1.5)

# Step 4:Decorations
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
              xlabel='Area', ylabel='Population')

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title("Bubble Plot with Encircling", fontsize=22)
plt.legend(fontsize=12)
plt.show()
plt.savefig('./语法基础/res/image/气泡图1.png')