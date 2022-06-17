#综合函数库

import datetime #时间库
import database #数据库操作（自定义函数）
import webworm  #爬虫
import notify   #通知操作
import sqlite3 as sql #SQL

#获得key函数
def getkey(platform):
    db=sql.connect("data/data.db")
    cur=db.cursor()
    cur.execute("SELECT key FROM Notify where platfrom =%d"% platform)
    key=cur.fetchall
    return key
    

#Nowtime
def nowtime():
    time=datetime.datetime.now()
    time=time.strftime('%Y-%m-%d %H:%M:%S')
    return time

