# 股票舆情监控

StockSentimentMonitor 是一个基于 Python 的股票舆情监控系统。它可以根据提供的股票名称抓取近期的舆情信息，对负面舆情进行筛选，并将舆情数据存储到数据库中。此外，它还可以通过邮件发送舆情监控结果。

## 功能

- 抓取股票的舆情信息
- 对负面舆情进行筛选
- 将舆情信息存储到数据库中
- 通过邮件发送舆情监控结果

## 安装

1. 克隆或下载此仓库到本地：
git clone https://github.com/your_username/StockSentimentMonitor.git
2. 使用pip安装依赖：
pip install -r requirements.txt（未更新requirement，不知咋整）

## 使用方法

1. 在src/config.py文件中配置邮件服务器信息（如：EMAIL_HOST，EMAIL_PORT，EMAIL_USER，EMAIL_PASSWORD）、收件人（TO_EMAIL）、监控的股票清单（STOCK_LIST）。
2. 运行main.py文件，程序将自动抓取股票舆情信息并通过邮件发送负面舆情监控结果。

python src/main.py

## 贡献者
无

## 许可证
本项目遵循 MIT 许可证。
