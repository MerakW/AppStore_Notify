#实现通知推送

from nturl2path import url2pathname
import webworm
import func
import database
import requests

#Bark平台推送
def barking(text: str,title: str = "",pic: str = "",tone: str = "",prior: int = 0,url:str = ""):
    assert(isinstance(prior,int))
    levels = ["active","timeSensitive","passive"]
    level = levels[prior]
    if text == "":    #判断是否为空消息
        return "无法推送空信息"
    else:
        #key=database.getkey("bark")
        key="2ABRBxppmz8nHDFevrRSq9"
        if title == "":
            bark = requests.get("https://api.day.app/%s/%s?sound=%s&icon=%s&level=%s&url=%s" %(key,text,tone,pic,level,url2pathname))    #使用Request库发送get请求推送
        else:
            bark = requests.get("https://api.day.app/%s/%s/%s?sound=%s&icon=%s&level=%s&url=%s" %(key,title,text,tone,pic,level,url2pathname))    #使用Request库发送get请求推送
        if bark.ok:
            return "Success"
        else:
            return "Failed,Error Code:%s"  %(bark.reason)
        
barking(text="test",title="testtitle",prior=1,url="https://baidu.com")
barking("text")


