# %%
from bs4 import BeautifulSoup
import requests

# incorperate a bool / variavble to goto next page
cd_gov = 'https://open.canada.ca/data/en/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412'
g_soup = requests.get(cd_gov)
ugly_soup = BeautifulSoup(g_soup.text)

# %%
for string in ugly_soup.find_all('a'):
    if string.get('href').endswith('.csv'):
        print(string.get('href'))

# %%
if 

