### 重定向：把应该输出到终端的内容写入文件中
# 例如：ls -lh > a                 将文件列表信息输入到文件a中

## >            覆盖到文件中
## >>           追加到文件中

### echo：将输入的内容再次返回终端
# 例如：echo：Hello >> a            将Hello追加到文件a中

### 管道：Linux允许一个命令的输出通过管道作为下一个命令的输入
# 例如：ls -lh|more                 将文件列表的结果分屏显示

## 常用包括more、grep

