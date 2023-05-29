import csv
import requests
from tqdm import tqdm
import random
import time
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import os
from glob import glob


all_pngs = glob('data/all_images/early_modern_images/png_final/*.png')
out_items = list()

for item in all_pngs:
    item_id = item.split('.')[0].split('/')[-1]
    line = dict()
    line['page_id'] = item_id
    line['ecco_id'] = item_id[:-5]
    line['page_number'] = int(item_id[-5:-1])
    line['allas_url'] = (
        "https://a3s.fi/dhh23-em-pages/" + item_id + ".png")
    out_items.append(line)


with open("data/ecco_sci_urls.csv", 'w') as csvf:
    fieldnames = list(out_items[0].keys())
    writer = csv.DictWriter(csvf, fieldnames=fieldnames)
    writer.writeheader()
    for item in out_items:
        writer.writerow(item)
