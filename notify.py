#实现通知推送

import webworm
import func
import database
import requestssound

#Bark平台推送
def barking(text,title,pic,tone,prior):
    if text=="":
        return "无法推送空信息"
    else:
        key=database.getkey("bark")
        bark=requests.get("https://api.day.app/%S/%S/%S?sound=%S&icon=%S&")    