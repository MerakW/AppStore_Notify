
import sqlite3 as sql
import func

def newprice(appid: int, price: float): # 记录新的价格数据
    db = sql.connect("data/data.db")
    cur = db.cursor()
    nowtime = func.nowtime()    #获取当前时间
    command = (f"INSERT INTO Trace(appid,price,updatetime) VALUES({appid},{price},{nowtime})")  # 插入新的价格数据
    db.commit() # 提交修改
    cur.close() # 关闭游标
    db.close()  # 关闭数据库连接
    return True

def newapp(name: str, appid: int, platform: int, ):   # 记录新的App信息
    db = sql.connect("data/data.db")
    cur = db.cursor()
    command = (f"INSERT INTO App(name,appid,platform) VALUES('{name}',{appid},{platform})")  # 插入新的APP数据
    db.commit() # 提交修改
    cur.close() # 关闭游标
    db.close()  # 关闭数据库连接
    return True
    
