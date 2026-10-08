# %%
from bs4 import BeautifulSoup
import requests
import urllib.parse


# %%
class CrvList:

    def __init__(self, db_url):
        self.url = db_url
        self.soup = requests.get(self.url)
        self.beautiful_soup = BeautifulSoup(self.soup.text, features="html.parser")
        self.iterable_soup = self.beautiful_soup.find_all('a')
        self.hlength = len(self.iterable_soup)
        self.urls = set()
        # self.next_page = self.iterable_soup.text().capitalize() == 'Next'
    
    
    def __str__(self):
        return "\n\n".join(self.urls)


    def __repr__(self):
        pass


    def get_crvs(self):
        soup_vol = self.hlength   

        while soup_vol > 0:
            for string in self.iterable_soup:
                if string.get('href') is not None:    
                    if string.get('href').endswith('.csv'):
                        self.urls.add(string.get('href'))
                        soup_vol -= 1


    
    


# main_url = 'https://open.canada.ca/data/en/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412'

# crvs = CrvDb(main_url)
# crvs.get_crvs()
# print(list(crvs.urls)[-1] == list(crvs.urls)[8])

        