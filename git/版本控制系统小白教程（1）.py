# 前言：git中文文件名乱码问题

# 对于windows UTF-8字符集
# git config –global core.quotepath false

# 对于linux GBK字符集
# git config --global i18n.logOutputEncoding gbk      查看提交的中文说明
# git config --global i18n.commitEncoding gbk         提交时声明为中文

### 右键 git bash here 打开命令行窗口

### 关于版本

#  git --version                                   获取git版本
#  git update-git-for-windows                      升级最新版本

### 配置相关 global代表全局都有效 local意味本地仓库有效 system代表系统使用者有效

#  git config --global user.name "用户名"             配置全局用户名
#  git config --global user.email "邮箱地址"          配置邮箱
#  git config --global --list                        查看全局配置列表

### 创建仓库的方法

#  git init ：手动创建目录，直接将该目录变为git仓库

## 目录下 git bash here 输入 git init 生成隐藏文件夹.git 用于版本控制，不得修改其中任何内容

#  git init 仓库名 ：在该目录下创建一个仓库，且仓库内生成.git文件夹

### 提交版本
### 注意：工作区与暂存区 我们创建的版本库中有很多东西，其中包括这个暂存区。
### 提交版本时，其实是分两步进行的：1.将对文件的操作从工作区添加到暂存区 2.将暂存区操作提交到当前分支（创建git仓库时，会默认创建一个master分支）
### 另外的：版本控制系统只知道文本文件的改动，但像图片视频这些二进制文件，并不能准确获取其中的改变

#  git add <file>                                   单文件提交到暂存区
#  git add .                                        所有文件提交暂存区
#  git commit -m '提交信息'                          将暂存区文件提交git仓库
#  git log                                          查询历史提交记录

#  git commit -a -m '提交信息'                       所有文件提交暂存区同时提交仓库

### 查看版本状态

#  git status                                       查看工作区状态
#  git status -s                                    以简洁方式查看
#  git status --short                               同上

##  工作区干净
#   nothing to commit,working tree clean

##  工作区和暂存区不同步  相关文件会标红 使用restore可以回退至同暂存区一致状态
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)

##  文件已提交到暂存区但未同步到版本库  相关文件标绿 使用restore --staged可以回退至工作区已修改未提交状态
#   (use "git restore --staged <file>..." to unstage)

## 简洁状态信息如下：
#   ??    文件名                    文件新建，未添加至暂存区
#   A(绿) 文件名                    文件新建，已于暂存区，未提交库
#   M(红) 文件名                    文件被修改，未添加至暂存区
#   M(绿) 文件名                    文件被修改，已于暂存区，未提交库
#   无内容                          工作区tree干净

## N new    M modified

#### 比对

###  查看历史版本

#  git log                                          基本查看，拉取所有信息
#  git log -pretty=oneline                          只显示一行信息
#  git log -p                                       查看版本之间差别
#  git log -2                                       查看最近两个版本
#  git log -2 -p                                    查看最近两个版本之间的差别
#  git log --stat                                   查看大致的统计信息，以加减符号表示改动

### 工作区间对比
#  git diff                                         需要未提交storage的工作区内容

### 暂存区间对比
#  git diff --staged

### 版本间对比
#  git log                                           获取版本信息，哈希值
#  git diff 哈希值1 哈希值2

### 忽略特殊文件

## 工作区根目录下创建 .gitignore文件 写入配置后提交到仓库生效
## 内容类似正则表达式

#   #           注释
#   *           匹配0个或任意个字符
#   [abc]       匹配其中任意一个字符
#   [0-9]       0-9字符
#   ？          匹配任意一个字符
#   /           结尾指定目录（屏蔽某目录）
#   ！          取反（不屏蔽）

## 强制提交 被忽略后，git add 时会报错
#  git add -f 文件名               可以做到强制提交的效果

## 规则检查 针对某个未提交成功的文件检查.gitignore文件是否写入这条规则
#  git check-ignore -v 文件名      会返回第几行屏蔽了该文件