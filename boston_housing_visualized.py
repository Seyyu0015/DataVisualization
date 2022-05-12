import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
波士顿房价数据可视化

"""

# 从csv中读取波士顿房价数据 前13列为特征 最后一列是target
boston_housing = pd.read_csv("csv/boston_house_prices.csv", header=0)

# 测试读取结果
# print(boston_housing)

# 转化为Numpy数组
housing = np.array(boston_housing)
# y为数据中的想要预测的目标数据
target = housing[:, 13]
# x为数据中的13个特征数据的所有值
features = housing[:, :13]

# 将所有属性与房价之间的关系可视化
plt.rcParams["font.family"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False

# 设置标题字段
titles = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE",
          "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"]

# 设置画布大小
plt.figure(figsize=(12, 12))

# 循环创建散点图 划分画布为4×4的子图
for i in range(13):
    plt.subplot(4, 4, (i + 1))
    plt.scatter(features[:, i], target)
    plt.xlabel(titles[i])
    plt.ylabel("Price($1000's)")
    plt.title(str(i + 1) + "." + titles[i] + "-Price")

plt.tight_layout()

# 设置总标题 显示画布
plt.suptitle("各个属性与房价的关系", x=0.5, y=1.02, fontsize=20)
plt.show()
