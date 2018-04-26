import configparser
from datetime import datetime
import requests
from feedgen.feed import FeedGenerator
from bs4 import BeautifulSoup
from pytz import timezone

config = configparser.ConfigParser()
config.read('config.ini')

for section in config.sections():
    s = dict(config.items(section))
    r = requests.get(s['url'])
    soup = BeautifulSoup(r.text, 'lxml')
    titles = soup.select(s['item_title'])
    dates = soup.select(s['item_date'])

    fg = FeedGenerator()
    fg.title(section)
    fg.description(section)
    fg.link(href=s['url'], rel='alternate')

    for i in range(len(titles)):
        fe = fg.add_entry()
        fe.title(titles[i].text)
        fe.link(href=titles[i].get('href'), rel='alternate')
        date = datetime.strptime(dates[i].text.strip(), s['item_date_format'])
        if config.has_option(section, 'item_timezone'):
            localtz = timezone(s['item_timezone'])        
            date = localtz.localize(date)

        fe.published(date)

    fg.rss_file(section.replace(' ', '_') + '.xml')
