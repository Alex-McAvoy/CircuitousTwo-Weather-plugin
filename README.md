# 关于

最近使用 Rainmeter 的 CircuitousTwo 插件，发现天气功能由于其给出的站点已停止服务，无法显示当前天气，为此对配置文件进行了一些更改

该站点可提供天气服务：http://tianqi.2345.com/today-54823.htm

查看其 Robot.txt 后发现其允许爬取天气相关信息，因此写了一个爬虫对该页面的天气相关信息进行正则语言测试

测试完成后，对 CircuitousTwo 插件的 yweather.ini 进行修改，使得其可以成功显示天气

# 效果图

鼠标移出

![unload successfule](https://github.com/Alex-McAvoy/CircuitousTwo-Weather-plugin/blob/master/images/mouseout.png)

鼠标移入

![unload successfule](https://github.com/Alex-McAvoy/CircuitousTwo-Weather-plugin/blob/master/images/mouseover.png)

# 使用说明

1. 在 Rainmeter 安装 CircuitousTwo 插件后，将 weather 文件夹整体复制进 CircuitousTwo 皮肤目录，将原有的 yweather.ini 进行替换
2. 根据自己的城市，在提供天气的站点中寻找相应城市
3. 编辑 yweather.ini，将 URL 替换为相应城市的 URL
4. 在 [Rainmeter] 段中，将 MouseLeaveAction 属性值 [!SetOption subText Text "Jinan,Shandong"] 中的 "Jinan,Shandong" 设为相应城市名称
5. 保存后刷新桌面的天气插件即可

# 问题说明

1. 刷新后仍无变化，请利用所给的 Spider 自己测试正则表达式，将测试好的正则表达式替换到 RegExp 即可
2. 乱码，根据网页的 <meta> 标签所给的编码，设置相应的 CodePage 属性

关于 CodePage 代码编号，详见：

# 桌面整体效果
