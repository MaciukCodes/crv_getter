from crv_utils import CrvDb

main_url = 'https://open.canada.ca/data/en/dataset/2916fad5-ebcc-4c86-b0f3-4f619b29f412'

crvs = CrvDb(main_url)
crvs.get_crvs()
print(crvs)