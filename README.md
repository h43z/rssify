I looked at a few online services that provide custom created RSS feeds
for websites that don't have one. None of them were free of charge 
without being too much limited in functionality for me.

So I hacked together this very simple rssify.py script.
It reads from a config file your websites you want to rssify.
It could be easily extened for more features if needed.
For now it only parses the title and date via css selectors and generates
a feed.xml file which can be imported into newsboat/newsbeuter or I guess any
other rss reader.

```config.ini
[Jodel Engineering Blog]
url = https://jodel.com/engineering/
item_title = .post-title > a
item_date = .post-date
item_date_format = %%b %%d, %%Y
item_timezone = Europe/Berlin
```

The script runs once daily in a cronjob on my local machine.
