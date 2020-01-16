"""
有若干个学生信息如下,将这些学生信息插入到cls表
      [('Dave',17,'m',81),
       ('Ala',18,'w',84),
       ('Eva',19,'w',91)]
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 生成游标对象 (操作数据库,执行sql语句,获取结果)
cur = db.cursor()

l = [('Dave',17,'m',81),
       ('Ala',18,'w',84),
       ('Eva',19,'w',91)]
sql = "insert into cls (name,age,sex,score) values " \
      "(%s,%s,%s,%s);"
try:
    # for i in l:
    #    cur.execute(sql,i)
    cur.executemany(sql,l) # 执行多次sql语句
    db.commit()
except:
    db.rollback()


# 关闭游标和数据库连接
cur.close()
db.close()