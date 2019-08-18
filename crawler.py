import feedparser

rss_url = 'https://news.google.com/rss?hl=zh-TW&gl=TW&ceid=TW:zh-Hant'
 
# 抓取資料
data = feedparser.parse(rss_url)

for i in data['entries']:
	print(i['title'])
	print(i['link'])