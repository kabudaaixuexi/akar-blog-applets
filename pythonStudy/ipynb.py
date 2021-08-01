import requests
from bs4 import BeautifulSoup
import time
import re
import numpy as np
N=58  
b=[]
c1=[]
c3=[]
for i in range(N):
    url1='https://gouwu.sogou.com/shop?display=grid&query=%C4%CC%D6%C6%C6%B7&host=sogou.com&isAbroad=0&rank=0&pid=sogou-navi-88f334ae12274afe&priceDown=0&attr=1357224&interV=&priceLowest=0&page='+str(i+1)+'&sourceid=sr_bpage&interV='
    rqq = requests.get(url1)
        # ('https://gouwu.sogou.com/shop?query=%C4%CC%D6%C6%C6%B7&isAbroad=0&host=sogou.com&rank=0&priceLowest=0&pid=sogou-navi-88f334ae12274afe&priceDown=0&attr=1357224&display=grid&sourceid=sr_sxsx&interV=')
    soup = BeautifulSoup(rqq.content,'lxml')
    c2 = []
    for i in range(len(soup.select('#sResultList>div>h4'))):
        url='#sr_r_all_809_'+str(i)+'> div.item_price > span.item_price_sale'
        time.sleep(0.05)
        print(i)
        c2.append(str(soup.select(url)))
    c1.append([i.text for i in soup.select('#sResultList>div>h4')])
    c3.append([i.text for i in soup.select('#sResultList>div>div>em')])
    for i in range(len(c2)):
        if c2[i]!='':
            b1=c2[i][31:]
            b.append(re.sub(pattern='</span>]',repl='',string=b1))
        else:
            b.append('0')

a=list(np.array(c1).ravel())
c=list(np.array(c3).ravel())