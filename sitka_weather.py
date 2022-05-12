import csv
from matplotlib import pyplot as plt
from datetime import datetime

"""
使用折线图显示温度

"""
# 读取csv文件
with open('csv/sitka_weather.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 创建用于储存温度的列表
    dates, highs, lows = [], [], []

    # 将数据添加到列表内
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)

# 根据列表数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# 设置标题
plt.title("High and low temperatures", fontsize=27)
# x轴名称
plt.xlabel('Month', fontsize=22)
# y轴名称
plt.ylabel('Temperature(F)', fontsize=16)
# 格式
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
