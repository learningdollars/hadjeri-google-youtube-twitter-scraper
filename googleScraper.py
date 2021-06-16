import feedparser
from bs4 import BeautifulSoup
from datetime import datetime as dt





def clean(html):
    '''
    Get the text from html and do some cleaning
    '''
    soup = BeautifulSoup(html,"lxml")
    text = soup.get_text()
    text = text.replace('\xa0', ' ')
    return text

def google_scrape(topic,size):
    '''
    Parse the URL, and print all the details of the news
    '''
    scrapurl = f"http://news.google.com/news?q={topic}-19&sort=date&num={size}&output=rss"
    feeds = feedparser.parse(scrapurl).entries
    for f in feeds:

        description = clean(f.get("description", ""))
        date = dt.strptime(
            f.get("published", ""), '%a, %d %b %Y %H:%M:%S %Z')
        title = f.get("title", "")
        url = f.get("link", "")
        print(description,date, title, url)




