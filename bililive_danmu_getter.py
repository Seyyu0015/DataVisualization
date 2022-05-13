from bilibili_api import live, sync, user
# 获取时间并格式化
import time
time = time.strftime("%Y-%m-%d_", time.localtime())

# 创建直播间对象
room = live.LiveDanmaku(int(input('直播间id：')))


# 弹幕触发方法
@room.on('DANMU_MSG')
async def on_danmaku(event):
    with open('csv/' + time + 'danmu' + '.txt', "a") as f:
        f.write(event['data']['info'][1])


sync(room.connect())
