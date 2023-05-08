'''
cat             查看文件内容，创建文件，文件合并，追加文件内容
more            分屏显示文件内容
grep            搜索文本文件内容
'''


## cat一次显示所有内容，适合内容较少的文本
## more分屏显示，适合显示较多内容的文本

# more下一些操作键
# 回车     向下一行
# 空格     翻页
# b       向上翻页
# f       向下翻页
# q       退出



## cat -b           输出非空内容的行号（nl命令与其等价）
## cat -n           输出所有内容的行号


### grep as 123.txt         在123.txt的文件中匹配as 输出该行内容并标红匹配的内容

## grep -n          显示对应内容行号
## grep -v          显示不匹配内容的相关行内容
## grep -i          忽略大小写

# 注意：搜索内容包含空格时，需要引号包裹

### grep模式查找

## grep ^f 123.txt              匹配所有f开头的行
## grep ge$ 123.txt             匹配所有ge结尾的行