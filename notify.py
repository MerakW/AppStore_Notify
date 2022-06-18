# 实现通知推送

from nturl2path import url2pathname
import requests

# Bark平台推送


def barking(text: str, title: str = "", pic: str = "", tone: str = "", prior: int = 0, url: str = "") -> str:
    assert(isinstance(prior, int))
    levels = ["active", "timeSensitive", "passive"]
    level = levels[prior]
    if text == "":  # 判断是否为空消息
        return "无法推送空信息"
    else:
        #key=database.getkey("bark")
        key = "2ABRBxppmz8nHDFevrRSq9"
        print(title)
        if title.__len__() != 0:
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


barking(text="test", title="testtitle", prior=1, url="https://baidu.com")
