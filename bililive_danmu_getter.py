from bilibili_api import live, sync, user
import time

"""
哔哩哔哩直播（Bililive）指定直播间单日弹幕单字出现频率柱状图
获取弹幕脚本

"""
time = time.strftime("%Y-%m-%d_", time.localtime())
room = live.LiveDanmaku(int(input('直播间id：')))


# 弹幕触发方法
@room.on('DANMU_MSG')
async def on_danmaku(event):
    with open('csv/' + time + 'danmu' + '.txt', "a") as f:
        f.write(event['data']['info'][1])


sync(room.connect())
