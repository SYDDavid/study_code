'''
cur.fetchall    方法返回为元组嵌套元组
当我们希望结果为dict时，可以通过改变connect参数实现：
    cursorclass=pymysql.cursors.Dictcursor
cur.fetchall    方法返回为列表嵌套字典
'''

import pymysql

# 1.建立连接
conn = pymysql.connect(
    host='api.lemonban.com',
    port=3306,
    user='future',
    password='123456',
    # 可以在连接时指定，也可以在查询语句中指定
    database='futureloan',
    # 建议使用utf8用utf-8可能会报错
    charset='utf8',
    cursorclass=pymysql.cursors.Dictcursor
)

# 2.创建游标
cur = conn.cursor()

# 3.执行sql语句

sql = 'select * from member where mobile_phone="13030780869"'
count = cur.execute()  # 此处返回为查询结果总数

# 4.获取结果
cur.fetchone()  # 获取当前这一条
cur.fetchmany()  # 获取当前往后若干条
cur.fetchall()  # 获取剩下所有

# 5.关闭游标，关闭连接
cur.close()
conn.close()
