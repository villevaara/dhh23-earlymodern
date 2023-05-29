import pandas as pd
import zipfile
from tqdm import tqdm


merged_df = pd.read_csv("data/merged_all.csv", dtype={"ecco_id": str, "page_id": str})
bot_img = merged_df[merged_df['category_clip'] == "botanical"][ 'page_allas_url']
bot_list = bot_img.tolist()
botfiles = ["/scratch/project_2007773/early_modern/illustration/" + f for f in bot_list]


with zipfile.ZipFile('botanical_ill.zip', 'w') as zipMe:
    for file in tqdm(botfiles):
        zipMe.write(file, compress_type=zipfile.ZIP_DEFLATED)
