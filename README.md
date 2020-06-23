# 说明

最近使用月饼老师推荐的 Rainmeter 优化了下桌面，在使用 CircuitousTwo 插件时，发现天气功能由于其给出的站点已停止服务，无法显示当前天气，为此对配置文件进行了一些更改

在1.0版本中，利用 (2345天气网)[http://tianqi.2345.com/today-54823.htm] 站点提供的天气服务来获取天气相关信息

在利用编写的爬虫测试完成后，对 CircuitousTwo 插件的 yweather.ini 进行修改，使得其可以成功显示天气

在2.0版本中，利用免费天气api接口：(点击这里)[https://www.sojson.com/blog/305.html]来获取天气相关信息

在此对提供api的作者进行感谢

ps：
1. v1.0位于主分支
2. v2.0位于2.0分支

~~由于月饼老师非 CS 专业，没有 GitHub 账号，就不艾特了...~~

# 效果图

## V1.0

整体效果图

![load unsuccessful](https://github.com/Alex-McAvoy/CircuitousTwo-Weather-plugin/blob/master/images/entirety.png)

天气插件鼠标移出

![load unsuccessful](https://github.com/Alex-McAvoy/CircuitousTwo-Weather-plugin/blob/master/images/mouseout.png)

天气插件鼠标移入

![load unsuccessful](https://github.com/Alex-McAvoy/CircuitousTwo-Weather-plugin/blob/master/images/mouseover.png)

## v2.0

![load unsuccessful](https://github.com/Alex-McAvoy/CircuitousTwo-Weather-plugin/blob/v2.0/images/entirety.png)

天气插件鼠标移出

![load unsuccessful](https://github.com/Alex-McAvoy/CircuitousTwo-Weather-plugin/blob/v2.0/images/mouseout.png)

天气插件鼠标移入

![load unsuccessful](https://github.com/Alex-McAvoy/CircuitousTwo-Weather-plugin/blob/v2.0/images/mouseover.png)

# 使用说明

## v1.0

1. 在 Rainmeter 安装 CircuitousTwo 插件后，将 weather 文件夹整体复制进 CircuitousTwo 皮肤目录，将原有的 yweather.ini 进行替换
2. 根据自己的城市，在提供天气的站点中寻找相应城市
3. 编辑 yweather.ini，将 URL 替换为相应城市的 URL
4. 在 [Rainmeter] 段中，将 MouseOverAction 属性值 [!SetOption subText Text "Jinan,Shandong"] 中的 "Jinan,Shandong" 设为相应城市名称
5. 保存后刷新桌面的天气插件即可

## v2.0

1. 在 Rainmeter 安装 CircuitousTwo 插件后，将 weather 文件夹整体复制进 CircuitousTwo 皮肤目录，将原有的 yweather.ini 进行替换
2. 根据自己的城市，寻找相应城市的城市代码
3. 编辑 yweather.ini，将 URL 最后的城市代码替换为相应城市的城市代码
4. 保存后刷新桌面的天气插件即可

# 问题说明

1. 刷新后仍无变化，请利用所给的 Spider 自己测试正则表达式，将测试好的正则表达式替换到 RegExp 即可
2. 若出现乱码，根据网页的 <meta> 标签所给的编码，设置相应的 CodePage 属性

关于 CodePage 代码编号，详见：https://alex-mcavoy.github.io/practical-skills/e9e520a4.html
