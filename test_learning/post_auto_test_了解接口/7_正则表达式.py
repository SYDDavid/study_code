'''
字符串：正则表达式(regular)
    使用：
        1、re.match(regular,str)         从头匹配，若其第一个不一致，则失败
        2、re.search(regular,str)        包含匹配，若其中存在匹配的，则成功
        3、re.findall(regular,str)       匹配所有合适的字符串，并列表形式返回
        4、re.sub(regular,str,new_str)   匹配并替换新字符串
    规则： 网址：https://tool.oschina.net/uploads/apidocs/jquery/regexp.html

    单规则匹配
        .	    匹配除“\n”之外的任何单个字符
        \d	    匹配一个数字字符。等价于[0-9]。
        \D	    匹配一个非数字字符。等价于[^0-9]。
        \w	    匹配包括下划线的任何单词字符。等价于“[A-Za-z0-9_]”        注意：这里支持中文！！
        \W	    匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。
        [xyz]	字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”。
        [^xyz]	负值字符集合。匹配未包含的任意字符。例如，“[^abc]”可以匹配“plain”中的“p”。
        [a-z]	字符范围。匹配指定范围内的任意字符。例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。
        [^a-z]	负值字符范围。匹配任何不在指定范围内的任意字符。例如，“[^a-z]”可以匹配任何不在“a”到“z”范围内的任意字符。

    多字符匹配
        {n}	    n是一个非负整数。匹配确定的n次。                        例如：'[abc]{3}'，规则则匹配例如abc，abb等
        {n,}	n是一个非负整数。至少匹配n次。
        {n,m}	m和n均为非负整数，其中n<=m。最少匹配n次且最多匹配m次。     注意：实际匹配中优先最大，最后考虑最小情况(默认：贪婪模式)

        *   	匹配前面的子表达式零次或多次。
        +	    匹配前面的子表达式一次或多次。
        ?	    匹配前面的子表达式零次或一次。

    边界限定：
        ^	    匹配输入字符串的开始位置。
        $	    匹配输入字符串的结束位置。

    规则扩充：
        x|y 	匹配x或y。

    匹配分组
        （）      将括号内容提取出来

算法扩充:
    贪婪模式：尽可能匹配更多的
    非贪婪模式：尽可能匹配最少的       {n,m}? 设定为非贪婪模式
'''

'''
'a\d+a'         a开头a结尾中间是数字且至少一个
'a(\d+)a'       a开头a结尾提取中间的数字内容
'''

import re

s = 'asdfa21234n2j1k4hkj1jh&%&%……笑死我了'

res = re.findall('.', s)
print(res)

res = re.findall('\d', s)
print(res)

res = re.findall('\w', s)
print(res)

res = re.findall('[abcd]', s)
print(res)

res = re.findall('[^a-d]', s)
print(res)

res = re.findall('[a-d]{3}', 'abcabdbbabdbajjbsdjabf')
print(res)

res = re.findall('[a-d]{2,}?', 'abcabdbbabdbajjbsdjabf')
print(res)

res = re.findall('a(.*?)a', 'abcabdbbabdbajjbsdjabf')
print(res)

res = re.findall('a(.*)a', 'abcabdbbabdbajjbsdjabf')
print(res)