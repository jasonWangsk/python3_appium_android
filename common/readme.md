#common：存放工具类的脚本；
1、生成htmlreport 工具类
2、识别图片信息后存到本地
3、图片识别
4、截取图片后裁剪尺寸-识别
5、读取config配置文件
6、封装截图方法


启动appium
启动appium：appium -a 127.0.0.1 -p 4723 --log xxx.log --local-timezone

-p 4723 指定端口

--log xxx.log指定日志保存到指定文件内（可以是绝对路径）

--local-timezone指定时间为本地时间

--log-level error设置日志级别，默认是debug
win平台在命令的开始添加start /b，mac平台在命令的末尾添加&：表示后台启动，不加时，后续的程序无法运行(终端单独启动时可以不加)

//
https://www.jianshu.com/p/83878bc0870c