import time
import datetime
import dateutil.parser

### 获取当前时间的数字

before = time.time()  # 获取的是当前时间的秒时间(从1970年1月1日0时开始计算)
time.sleep(0.5)
after = time.time()

print(after - before)

print('*' * 50)

### 指定格式字符串显示时间

# 获取当前时间

print(datetime.datetime.now())

# datetime的格式化

print(datetime.datetime.now().strftime('%Y-%m-%d ** %H:%M:%S'))

# time的格式化

print(time.strftime('%Y-%m-%d ** %H:%M:%S', time.localtime()))

print('*' * 50)

### 秒时间转化为字符串时间

print(time.strftime('%Y-%m-%d ** %H:%M:%S', time.localtime(before)))

### 字符串时间转化为秒时间

print(int(time.mktime(time.strptime('2015-08-01 23:59:59', '%Y-%m-%d %H:%M:%S'))))

print('*' * 50)

### ISO格式转化为本地时间

# 字符串时间 转化为 datetime 对象
dt = dateutil.parser.isoparse('2008-09-03T20:56:35.450686+00:00')

# 转化为本地时区的 datetime 对象
localdt = dt.astimezone(tz=None)

# 产生本地格式 字符串
print(localdt.strftime('%Y-%m-%d %H:%M:%S'))

print('*' * 50)

### 获取某时间的各单位下具体内容

shijian = datetime.datetime.now()

print(shijian.year)
print(shijian.month)
print(shijian.day)
print(shijian.hour)
print(shijian.minute)
print(shijian.second)
print(shijian.microsecond)
print(shijian.weekday()) # 0表示周一 依次类推

print('*' * 50)

### 获取指定字符串的星期数

that_day='2001-2-25'
that_day_dt=datetime.datetime.strptime(that_day,'%Y-%m-%d') # 字符串格式转成datetime类型
print(that_day_dt.weekday())

print('*' * 50)

### 往后推算一段时间

thatDay = "2018-6-24"

theDay = datetime.datetime.strptime(thatDay, "%Y-%m-%d").date()

# 后推120天 就是 + timedelta(days=120)
target = theDay + datetime.timedelta(days=120)

print(target)
print(target.weekday())

# 前推120天 就是 - timedelta(days=120)
target = theDay - datetime.timedelta(days=120)

print(target)
print(target.weekday())

