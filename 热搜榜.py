from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import  ssl
ssl._create_default_https_context = ssl._create_unverified_context
context = ssl._create_unverified_context()
html=urlopen('https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6').read().decode('utf-8')
soup=bs(html,features='html.parser')
href=soup.find_all('td',{'class':"td-02"})
for h in href:
    print(h.get_text())
