'''
python对接各大数据库：http://testingpai.com/article/1596527686073

1、安装 pip install pymysql

使用：
    1、连接数据库 + 创建游标    conn = pymysql.connect(
                                    host=,
                                    port=,
                                    user=,
                                    password=,
                                    database=,          # 指定莫数据库，若不指定则需要在sql语句中指定
                                    charset=            # 注意：这是里utf8，而不是UTF-8
                            )
                            cur = conn.cursor()
    2、执行sql语句            count = cur.execute(sql)
    3、获取执行结果            cur.fetchone()          # 获取当前游标下数据
                            cur.fetchmany()         # 获取当前游标下及之后共n条数据
                            cur.fetchall()          # 获取剩下所有数据
    4、关闭游标，关闭连接       cur.close()
                            conn.close()

未指定到指定 cursorclass=pymysql.cursors.DictCursor
    fetchone            tuple格式         dict格式
    fetchmany/fetchall  tuple嵌套格式      list嵌套dict
'''

import pymysql

# 1、建立连接
conn = pymysql.connect(
    host="api.lemonban.com",
    port=3306,
    user="future",
    password="123456",
    database="futureloan",  # 指定莫数据库，若不指定则需要在sql语句中指定
    charset="utf8",  # 注意：这是里utf8，而不是UTF-8
    cursorclass=pymysql.cursors.DictCursor
)

# 2、创建游标
cur = conn.cursor()

# 3、执行sql语句
sql = "select * from member LIMIT 10"
count = cur.execute(sql)  # 返回结果为匹配的数据条数

# 4、获取sql语句执行后的结果
## 注意：游标过了以后不会重新返回！！
one = cur.fetchone()
many = cur.fetchmany()
all = cur.fetchall()

# 若需要增、删、改，修改后需提交事务
cur.execute(sql)
conn.commit()

# 5、关闭游标与数据库
cur.close()
conn.close()
