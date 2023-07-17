'''
CI          持续集成
CD          持续交付

jenkins     持续集成的一种平台

代码检查 》》编译打包 》》单元测试 》》自动部署 》》冒烟测试 》》回归测试

jenkins可以定时 编译打包、自动部署

使用：
    1、用户目录运行cmd, 运行 java -jar jenkins.war --httpPort=8080
    2、在浏览器中, 使用http://127.0.0.1:8080 访问, 默认账号和密码为admin/admin

基本概念：job、workspace、plugin

job:
    任务/项目-打包、编译等具体任务
    job可以构建（执行该任务）
    有颜色之分                 蓝色：success 红色：fail 黄色：不稳定（历史记录中有fail记录）
    井号 #                    #n，代表历史共构建过多少次

workspace：
    默认是用来存放job相关的资料。例如：svn/git上自动下载代码，会自动存放到worksapce下对应job名称的文件夹中

plugin：
    插件安装，可不断扩展新功能

构建触发器：
    Build periodically:设置日程表
    MINUTE      0-59
    HOUR        0-23
    DOM         1-31
    MONTH       1-12
    DOW         0-7         0、7均表示周日

    例如：
        0 10 * * *              表示每天早上十点构建
        0 10 * * 1-5            表示工作日每日上午十点构建
        0 5，10 * * *           表示每天上午五点与上午十点构建
        0 10 * * 1-5/2          表示工作日每隔一天上午十点构建

video：52
'''