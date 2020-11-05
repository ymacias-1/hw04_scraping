import requests
import bs4
from bs4 import BeautifulSoup
import json 


keyword='keurig'

headers= {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'

}
try:
    results=[]
    for i in range(1,11):
        r=requests.get('https://www.ebay.com/sch/i.html?_nkw=' +keyword +'&_pgn='+str(i), headers=headers)
        r.status_code 
        r.text 
        #print(r.status_code)
        soup=BeautifulSoup(r.text, 'html.parser')
        boxes=soup.select('li.s-item--watch-at-corner.s-item')
        for box in boxes: 
            #print('-----')
            result={ }
            titles=box.select('.s-item__title')#put the CSS selector we want 
            for title in titles: 
                #print('title=',title.text)
                result['title']=title.text
            prices=box.select('.s-item__price')
            for price in prices: 
                #print('price=',price.text)
                result['price']=price.text
            statuses=box.select('.s-item__subtitle > .SECONDARY_INFO')
            for status in statuses: 
                #print('status=',status.text)
                result['status']=status.text
            #print(result)
            results.append(result)
    
    #print(len(results))

except: 
    pass
j=json.dumps(results)
with open('items.json', 'w') as f: 
    f.write(j)    
