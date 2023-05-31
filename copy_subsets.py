import pandas as pd
import zipfile
from tqdm import tqdm
import shutil


# merged_df = pd.read_csv("data/merged_all.csv", dtype={"ecco_id": str, "page_id": str})
new_clip = pd.read_csv("/scratch/project_2007773/early_modern/new_clip_classification.csv")

for category in list(set(new_clip['Category'])):
    cat_img = new_clip[new_clip['Category'] == category]['Image']
    cat_list = cat_img.tolist()
    catfiles = ["/scratch/project_2007773/early_modern/illustration/" + f for f in cat_list]
    for file in tqdm(catfiles):
        src_path = file
        dst_path = "/scratch/project_2007773/early_modern/ill_copy_new_clip/" + category + "/" + file.split('/')[-1]
        shutil.copy(src_path, dst_path)
