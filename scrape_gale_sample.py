import csv
import requests
from tqdm import tqdm
import random
import time
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import os


def download_png_url(url, savepath, error_log, success_log, skip_existing=True):
    saveloc = savepath + "/" + url.split('/')[-1].split('?')[0] + ".png"
    if skip_existing and os.path.exists(saveloc):
        pass
    else:
        time.sleep(random.randint(0, 2))
        s = requests.Session()
        retries = Retry(total=5,
                        backoff_factor=1,
                        status_forcelist=[500, 502, 503, 504])
        s.mount('https://', HTTPAdapter(max_retries=retries))
        resp = s.get(url)
        if resp.status_code == 200:
            with open(saveloc, 'wb') as f:
                f.write(resp.content)
            with open(success_log, 'a') as f:
                f.write(url + "\n")
        else:
            with open(error_log, 'a') as f:
                f.write(url + "\n")


def get_zero_padded_page_number(page_number):
    pn = str(page_number)
    while len(pn) < 4:
        pn = "0" + pn
    return pn


gale_pages_csv = "data/ecco_science_illustrations.csv"
gale_url_start, gale_url_end = "https://callisto.ggsrv.com/imgsrv/FastFetch/UBER2/", "?format=png"


gale_items = list()
with open(gale_pages_csv, 'r') as csvf:
    reader = csv.DictReader(csvf)
    for line in reader:
        item_id = line['ecco_id'] + get_zero_padded_page_number(line['page_number']) + "0"
        line['page_id'] = item_id
        line['gale_url'] = (gale_url_start +
                       item_id +
                       gale_url_end)
        line['allas_url'] = (
            "https://a3s.fi/early_modern/" +
            item_id +
            ".png"
        )
        gale_items.append(line)


random.seed("JepJep")
random_items = random.sample(gale_items, 10000)


with open("data/ecco_sci_urls.csv", 'w') as csvf:
    fieldnames = list(gale_items[0].keys())
    writer = csv.DictWriter(csvf, fieldnames=fieldnames)
    writer.writeheader()
    for item in gale_items:
        writer.writerow(item)


with open("data/random_sample.csv", 'w') as csvf:
    fieldnames = list(random_items[0].keys())
    writer = csv.DictWriter(csvf, fieldnames=fieldnames)
    writer.writeheader()
    for item in random_items:
        writer.writerow(item)


for item in tqdm(random_items):
    download_png_url(item['gale_url'], "data/images", "logs/err.log", "logs/success.log", skip_existing=True)
