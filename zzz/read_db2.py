"""
基于interest表,使用input输入一个学生的姓名,
获取该学生的姓名,爱好,价格信息.
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

# name = input("Name:")
# sql="select name,hobby,price " \
#     "from interest " \
#     "where name='%s';"%name

# sql="select name,hobby,price " \
#     "from interest " \
#     "where name=%s;"

sql = "select name,age,score from cls " \
      "where score>%s and age>=%s"

cur.execute(sql,[80,18]) #通过参数列表给sql语句传入值
print(cur.fetchall())


# 关闭游标和数据库连接
cur.close()
db.close()