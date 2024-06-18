
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://aif.ru/tag/globalnoje_potjepljenije'

response = requests.get(url)
print(response)

da = BeautifulSoup(response.text,"lxml")
print(da)


temp = da.find_all('div', 'list_item')
print(temp)

for i in temp:
  print(i)

    
def pars(): 
    dict_news = {"news": [], "links": [], 'imgs': [], 'date': [] }

    for i in temp:
        dict_news['news'].append(i.find('span', 'item_text__title').text)
        dict_news["links"].append(i.find('a').get('href'))
        dict_news["imgs"].append(i.find('a', 'img_box no_title_element_js').find('img').get('src'))
        dict_news["date"].append(i.find('span', 'text_box__date').text)

    df_news = pd.DataFrame(dict_news, columns=["news", 'links', "imgs", 'date'])
    
    return(dict_news)


    


