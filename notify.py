#实现通知推送

import webworm
import func
import database
import requests

#Bark平台推送
def barking(text,title,pic,tone,prior):
    key=getkey(bark)
    