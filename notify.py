# 实现通知推送

from nturl2path import url2pathname
import requests
import sqlite3 as sql

# Bark平台推送
def barking(text: str, title: str = "", pic: str = "", tone: str = "", prior: int = 0, url: str = "") -> str:
    assert(isinstance(prior, int))
    levels = ["active", "timeSensitive", "passive"]
    level = levels[prior]
    if text == "":  # 判断是否为空消息
        return "无法推送空信息"
    else:
        db = sql.connect("data/data.db")    # 连接数据库
        cur = db.cursor()   # 获取游标
        command = "SELECT key FROM Notify where platform ='bark'"   # 查询key
        cur.execute(command)    # 执行查询
        key = cur.fetchone()    # 获取结果
        key = str(key)  # 转换为字符串
        key = key[2:-3] # 去除多余的字符
        cur.close() # 关闭游标
        db.close() # 关闭数据库
        print(key)
        print(title)
        if title.__len__() != 0:    # 判断是否有标题
            # 如果有标题，则添加标题
            info = {
                "sound": tone,
                "icon": pic,
                "level": level,
                "url": url2pathname
            }

            bark = requests.get(
                f"https://api.day.app/{key}/{text}", params=info)   # 请求推送
            print(bark.text)    # 打印返回结果
            return "推送成功"   # 返回推送成功

        else:
            info = {
                "sound": tone,
                "icon": pic,
                "level": level,
                "url": url2pathname
            }

            bark = requests.get(
                f"https://api.day.app/{key}/{text}", params=info)
            print(bark.text)
            return "推送成功"


barking("test",title="uwhfiehfuowhfoiwhf")