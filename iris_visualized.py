import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
鸢尾花数据集可视化

"""

# 读取鸢尾花数据集，数据集一共150个样本，4个属性，1个标签
COLUMN_NAMES = ["SepalLength", 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
df_iris = pd.read_csv("csv/iris.csv", names=COLUMN_NAMES, header=0)

# 测试读取结果
# print(df_iris)

# 转化为Numpy数组
iris = np.array(df_iris)

# 绘图
fig = plt.figure('Iris Data', figsize=(25, 25))
plt.suptitle("Anderson's Iris Data Set\n(Bule:Setosa | Red:Versicolor | Green:Virginica")
for i in range(4):
    for j in range(4):
        plt.subplot(4, 4, 4 * i + (j + 1))
        # 当i=j时，在绘图区域输出当前属性的名称
        if i == j:
            plt.text(0.3, 0.4, COLUMN_NAMES[i], fontsize=15)
        else:
            # 切片获得花瓣长度
            iris_len = iris[:, j]
            # 花瓣宽度
            iris_wid = iris[:, i]
            # 花的种类
            iris_type = iris[:, 4]

            plt.scatter(iris[:, j], iris[:, i], c=iris_type, cmap='brg')
        if i == 0:
            # 子图标题输出当前横坐标的属性名称，作为所有行的横坐标标签
            plt.title(COLUMN_NAMES[j])
        if j == 0:
            plt.ylabel(COLUMN_NAMES[i])

# 调整子图间距
plt.tight_layout()
plt.show()
