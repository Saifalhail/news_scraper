import newspaper
from newspaper import Article
from datetime import datetime

list_of_urls_mena = ['https://www.aljazeera.com/news/2022/12/6/n-korea-orders-new-artillery-firings-over-us-s-korea-drills',
				'https://www.aljazeera.com/news/2022/12/5/un-delays-decision-on-myanmar-representation-over-russian-stance',
				'https://www.aljazeera.com/news/2022/12/3/u-s-unveils-new-700m-high-tech-b-21-stealth-bomber',
                'https://www.bbc.com/news/world-europe-63857451']

list_of_urls_int = ['https://www.aljazeera.com/economy/2022/12/13/chinese-property-tycoon-accused-of-bribing-officials-in-us',
                'https://www.aljazeera.com/economy/2022/12/13/ftxs-bankman-fried-arrested-in-the-bahamas-as-us-unveils-charges',
                'https://www.aljazeera.com/economy/2022/12/12/cvs-walgreens-finalise-10bn-in-deals-to-settle-opioid-lawsuits']

list_of_urls_proc = ['https://www.aljazeera.com/sports/2022/12/12/can-morocco-win-the-world-cup',
                'https://www.aljazeera.com/news/2022/12/11/the-ten-talking-points-of-the-world-cup-so-far',
                'https://www.aljazeera.com/sports/2022/12/12/the-freestyle-footballer-with-a-difference-wowing-world-cup-fans']

extracted1 = {'articles': []}
extracted2 = {'articles': []}
extracted3 = {'articles': []}

for url in list_of_urls_mena:
    article = newspaper.Article(url="%s" % (url), language='en')
    article.download()
    article.parse()
    if article.publish_date is not None:
        publish_date = datetime.strptime(str(article.publish_date), '%Y-%m-%d %H:%M:%S').strftime('%d-%b-%Y')
    obj = {'title': article.title, 'top_image': article.top_image, 'publish_date': publish_date, 'url': article.url}
    extracted1['articles'].append(obj)

for url in list_of_urls_int:
    article = newspaper.Article(url="%s" % (url), language='en')
    article.download()
    article.parse()
    if article.publish_date is not None:
        publish_date = datetime.strptime(str(article.publish_date), '%Y-%m-%d %H:%M:%S').strftime('%d-%b-%Y')
    obj = {'title': article.title, 'top_image': article.top_image, 'publish_date': publish_date, 'url': article.url}
    extracted2['articles'].append(obj)

for url in list_of_urls_proc:
    article = newspaper.Article(url="%s" % (url), language='en')
    article.download()
    article.parse()
    if article.publish_date is not None:
        publish_date = datetime.strptime(str(article.publish_date), '%Y-%m-%d %H:%M:%S').strftime('%d-%b-%Y')
    obj = {'title': article.title, 'top_image': article.top_image, 'publish_date': publish_date, 'url': article.url}
    extracted3['articles'].append(obj)