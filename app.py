"""
Packages to install
pip install beautifulsoup4
pip install lxml
pip install requests


"""
from bs4 import BeautifulSoup
import requests
import csv

# with open('sample.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())  # will show ordered tags and nested tags
"""
Get html tags content 
"""

# match = soup.title.text
# match = soup.div
# match = soup.find('div')
# match = soup.find('div', class_='footer')
# article = soup.find('div', class_='article')
# # print(article)
# headline = article.h2.a.text
# summary = article.p.text
# print(headline)
# print(summary)

"""
Get all tags 
"""
# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     summary = article.p.text
#     print(headline)
#     print(summary)
#     print('********************')

"""
Now real world example website scraping
URL: https://coreyms.com

"""


def get_single_article():
    source = requests.get('https://coreyms.com').text
    soup = BeautifulSoup(source, 'lxml')
    article = soup.find('article')
    headline = article.h2.a.text
    print(headline)
    try:
        summary = article.find('div', class_='entry-content').p.text
        print(summary)

    except AttributeError:
        print('NoneType object has no attribute p')

    vid_src = article.find('iframe', class_='youtube-player')['src']
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    # print(vid_id)
    """
    make youtube video link
    """
    # using formatting string format which is available in Python 3.6
    # in older varsion use format method
    youtube_link = f'https://youtube.com/watch?v={vid_id}'
    print(youtube_link)
    print('***************************************************')
    print('***************************************************')


# get_single_article()


def get_all_articles():
    source = requests.get('https://coreyms.com').text
    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('cms_scrape.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline', 'summary', 'youtube_link'])

    for article in soup.find_all('article'):
        headline = article.h2.a.text
        print(headline)
        summary = article.find('div', class_='entry-content').p.text
        print(summary)
        try:
            vid_src = article.find('iframe', class_='youtube-player')['src']
            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]
            youtube_link = f'https://youtube.com/watch?v={vid_id}'

        except Exception as e:
            youtube_link = None

        print(youtube_link)
        print('***************************************************')
        csv_writer.writerow([headline, summary, youtube_link])
    csv_file.close()


get_all_articles()














