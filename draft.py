import re

str = '我们'
s = []
s1 = None

if re.findall('\d', str):
    print('true')
else:
    print('false')
