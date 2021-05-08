from bs4 import BeautifulSoup
import requests
import warnings

warnings.filterwarnings('ignore')

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

URL = 'https://justlightnovels.com/'
count = 1


def getPage(url, pages):
    global count
    if count <= pages:
        html = requests.get(url, verify=False)
        bs = BeautifulSoup(html.text, 'html.parser')
        print('*'*20) 
        print('PAGE {}'.format(count))
        print('*'*20) 
        articles = getArticles(bs)
        if articles == []:
            print('empty list')
        else:
            for article in articles: 
                print(article)
        count += 1
        newurl = '{}page/{}/'.format(url[:28], count)
        getPage(newurl, pages)



def getArticles(bs):
    articleList = []
    articles = bs.find('main', {'id': 'content'}).find_all('article')
    for article in articles:
        item = article.find('a')['title']
        articleList.append(item)

    return articleList

getPage(URL, 5)
