25/8/31前

mysql+线程池+http请求爬取+ip代理
日志显示，错误显示在数据库
数据库下发任务，修改状态，包括筛选条件下发,动态采集页数-最大前10页，最大重试3次


数据库配置：config.ini
数据库操作脚本：mysql.py
采集脚本：basic_main.py  detail_collector.py
数据库创建：58租房.sql
任务失败：数据库重试3次，且状态为0就是失败

部署：pycharm，python，mysql, navicat本地，运行视频

代理池：巨量ip包时，不能开其他静态代理，需要加自己ip白名单，需要届时开启，买包量或者包时