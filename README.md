# 说明

最近使用 Rainmeter 的 CircuitousTwo 插件，发现天气功能由于其给出的站点已停止服务，无法显示当前天气，为此对配置文件进行了一些更改

该站点可提供天气服务：http://tianqi.2345.com/today-54823.htm

查看其 Robot.txt 后发现其允许爬取天气相关信息，因此写了一个爬虫对该页面的天气相关信息进行正则语言测试

测试完成后，对 CircuitousTwo 插件的 yweather.ini 进行修改，使得其可以成功显示天气

