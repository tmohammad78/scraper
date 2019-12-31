import requests
from bs4 import BeautifulSoup


res=requests.get('https://news.ycombinator.com/newest')
# print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')
# print(link)

def create_custom(links,subtext):
    hn=[]
    for idx,item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote) :
            points = int(vote[0].getText().replace(' points', ''))
            hn.append({'title':title , 'link':href , 'votes':points})
    return hn


print(create_custom(links,subtext))