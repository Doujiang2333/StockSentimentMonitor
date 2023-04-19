# 股票舆情监控系统

本项目为股票舆情监控系统，用于抓取和分析股票相关新闻，并将负面舆情发送至指定邮箱。

## 安装

1. 克隆本仓库到本地：
git clone https://github.com/yourusername/stock-sentiment-monitor.git
2. 进入项目目录：
cd stock-sentiment-monitor
3. 安装项目依赖：
pip install -r requirements.txt
## 使用

1. 在 `config.py` 文件中配置邮件服务器相关信息。

2. 将股票持仓信息放在名为 `股票持仓统计.xlsx` 的 Excel 文件中。

3. 运行主程序：
python main.py

## 功能

1. 抓取新浪财经和腾讯财经上与指定股票相关的新闻。

2. 对新闻标题和内容进行情感分析。

3. 将负面舆情发送至指定邮箱。

## 注意事项

1. 本项目仅供学习交流使用，请勿用于商业目的。

2. 使用时请遵守相关法律法规，尊重他人知识产权。

3. 由于网站结构可能发生变化，本项目可能需要进行相应的维护和更新。

## 开源许可

本项目采用 MIT 许可。