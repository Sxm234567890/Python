import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置字体为支持中文的字体
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 创建一个有向图
G = nx.DiGraph()

# 添加节点
G.add_node("黑色旅游动机")
G.add_node("吸引力")
G.add_node("中心性")
G.add_node("自我表现")
G.add_node("认知形象")
G.add_node("情感形象")
G.add_node("总体形象")

# 添加有向边 (表示因果关系)
G.add_edge("黑色旅游动机", "吸引力")
G.add_edge("黑色旅游动机", "中心性")
G.add_edge("黑色旅游动机", "自我表现")
G.add_edge("吸引力", "认知形象")
G.add_edge("吸引力", "情感形象")
G.add_edge("中心性", "认知形象")
G.add_edge("中心性", "情感形象")
G.add_edge("自我表现", "认知形象")
G.add_edge("自我表现", "情感形象")
G.add_edge("认知形象", "总体形象")
G.add_edge("情感形象", "总体形象")

# 设置布局
pos = {
    "黑色旅游动机": (0, 2),
    "吸引力": (-1, 1),
    "中心性": (0, 1),
    "自我表现": (1, 1),
    "认知形象": (-1, 0),
    "情感形象": (0, 0),
    "总体形象": (0, -1)
}

# 绘制图形
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=12, font_weight="bold", arrows=True)

# 显示图形
plt.title("黑色旅游动机对旅游目的地形象的影响结构模型")
plt.show()
