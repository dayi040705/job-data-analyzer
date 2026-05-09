# 实习岗位数据分析与可视化平台

## 技术栈
Python + Selenium + Edge WebDriver + Pandas + Flask

## 功能
- 使用 Selenium 自动化采集实习僧网站 Java 实习岗位信息
- 通过 XPath 定位提取岗位名称、公司、薪资、城市、详情链接等字段
- 利用 Pandas 对数据进行清洗与统计分析（公司招聘活跃度排名、薪资分布）
- 使用 Flask 搭建 Web 服务，将分析结果通过 HTML 页面可视化展示

## 项目结构
- job_spider_v3.py — 爬虫主程序
- data_analysis.py — 数据分析脚本
- app.py — Flask Web 展示
- java_intern_jobs.csv — 爬取的数据
- company_ranking.csv — 公司排名统计结果

## 运行方式
1. 安装依赖：pip install selenium pandas flask
2. 下载 Edge WebDriver 并放在项目根目录
3. 运行爬虫：python job_spider_v3.py
4. 运行分析：python data_analysis.py
5. 运行 Web 服务：python app.py
6. 浏览器访问 http://127.0.0.1:5000
