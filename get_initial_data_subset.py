import zipfile
import csv
from glob import glob
from tqdm import tqdm


zip_path = "/scratch/project_2005072/ecco-images.zip"
out_path = "/scratch/project_2007773/early_modern/img/"
error_log = "logs/err_unzip_missing.log"

existing_files = glob(out_path + "*.TIF")
existing_files = [file.split("/")[-1] for file in existing_files]

zipf = zipfile.ZipFile(zip_path)

zipcont = zipf.namelist()

with open("data/ecco_sci_urls.csv", 'r') as csvf:
    reader = csv.DictReader(csvf)
    for line in tqdm(reader):
        fname = (line['page_id'] + ".TIF")
        if fname in existing_files:
            continue
        if fname not in zipcont:
            with open(error_log, 'a') as errf:
                errf.write(fname + "\n")
            continue
        f = zipf.open(fname)
        content = f.read()
        f = open(out_path + fname, 'wb')
        f.write(content)
        f.close()
