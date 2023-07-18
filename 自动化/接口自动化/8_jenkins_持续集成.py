'''
CI          持续集成
CD          持续交付

jenkins     持续集成的其中一种平台

jenkins有以下好处：
  * 1、自动化构建 ：可以根据预定义构建配置，从源代码库拉取最新代码，自动执行构建过程。
  * 2、持续集成   ：监控代码库变化，每次提交后或定期执行构建过程，以确保新代码没有错误。
    3、质量控制   ：静态代码分析，代码覆盖率，质量控制等任务。
  * 4、自动化部署 ：自动化的应用程序部署和配置管理。这包括将构建好的软件包部署到目标环境、配置服务器和应用程序参数等。
    5、可视化报告 ：监视管理构建过程，评价任务最近的执行晴雨表

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
        Poll SCM          :设置日程表，时间到了判断”源码“是否更新，若是，则构建
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

构建/构建后操作：需要安装不同插件去实现不同功能
    构建：执行py脚本，输入cmd命令行内容
        d:
        cd D:\Pychram-Workspace\Public_Python
        python D:\Pychram-Workspace\Public_Python\main.py

    构建后：
    1、展示HTML测试报告              注意：路径是相对于 workspace
        方案一：将代码放置于默认工作空间下
        方案二：修改默认工作空间

    jenkins呈现HTML报告需要安装兼容性插件：
        进入Manage Jenkis >>Script console
        System.setProperty("hudson.model.DirectoryBrowserSupport.CSP","")

    2、邮件发送：
    E-mail Notification
        构建成功不会发送邮件，构建失败才会

    Editable Email Notification
        1、配置全局发送人
            Manage Jenkis >> Configure System >> Jenkins Location >> 系统管理员邮件地址 >> 输入自己的邮件地址(2522337205@qq.com)
        2、配置邮件通知服务
            Manage Jenkis >> Configure System >> Jenkins Location >> 邮件通知 >> SMTP服务器 >> smtp.163.com(smtp.qq.com)
            点开高级 >> 勾选smtp认证 >> 输入账号密码   注意：密码为授权码
        （ssl端口：465 不开启ssl：25）
        3、配置插件内容 对应Editable Email Notification
            Manage Jenkis >> Configure System >> Jenkins Location >> Extended E-mail Notification
            点开高级 >> 勾选smtp认证 >> 输入账号密码   注意：密码为授权码
            与邮件通知服务保持一致

    邮件内支持传输附件               注意：路径是相对于 workspace
        Editable Email Notification >> Attachments



'''