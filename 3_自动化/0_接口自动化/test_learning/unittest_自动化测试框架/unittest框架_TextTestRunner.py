'''
TextTestRunner

with open('report.txt', 'w') as f:
    unittest.TextTestRunner(stream=f, verbosity=2).run(s1)

HTMLTestRunner

with open('report.html', 'w') as f1:
   HTMLTestRunner.HTMLTestRunner(stream=f1, verbosity=2).run(s1)

用例执行顺序：ASCII码顺序 0~9<A~Z<a~z
'''

import unittest
from HTMLTestRunner import HTMLTestRunner

s1 = unittest.TestLoader().discover(r'F:\code\测开之路\单元测试_unittest')

with open('report.txt', 'w') as f:
    unittest.TextTestRunner(stream=f, verbosity=2).run(s1)

with open('report.html', 'w') as f1:
   HTMLTestRunner.HTMLTestRunner(stream=f1, verbosity=2).run(s1)