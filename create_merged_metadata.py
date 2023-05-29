import pandas as pd


captions_df = pd.read_csv("data/illustration_captions.csv",
                          dtype={"ecco_id": str, "page_id": str})
captions_df = captions_df[['ecco_id', 'page_number', 'caption_texts']]

meta_sample = pd.read_csv("data/metadata_sample.csv",
                          dtype={"ecco_id": str, "page_id": str})

page_urls = pd.read_csv("data/ecco_sci_urls.csv",
                          dtype={"ecco_id": str, "page_id": str})


merged_df = pd.merge(page_urls, captions_df,  how='left', on=['ecco_id', 'page_number'])
merged_df.rename(columns={'allas_url': 'allas_page_url'}, inplace=True)
merged_df = pd.merge(merged_df, meta_sample,  how='left', on=['ecco_id'])
merged_df.rename(columns={'ecco_pages': 'number_of_pages'}, inplace=True)

illus_df = pd.read_csv('data/all_ill.txt', header=None)
illus_df.columns = ['page_allas_url']
illus_df['illustration_id'] = illus_df['page_allas_url'].str[:-4]
illus_df['page_id'] = illus_df['illustration_id'].str.split('_').str[0]
illus_df['illustration_allas_url'] = "https://a3s.fi/dhh23-em-illu/" + illus_df['page_allas_url']

merged_df = pd.merge(illus_df, merged_df,  how='left', on=['page_id'])

clip_pred_df = pd.read_csv("data/clip_predictions.csv")
clip_pred_df.columns = ['illustration_id', 'category_clip', 'score_clip']
clip_pred_df['illustration_id'] = clip_pred_df['illustration_id'].str[:-4]
em_pred_df = pd.read_csv("data/early_modern_predictions.csv")
em_pred_df.columns = ['illustration_id', 'category_em']
em_pred_df['illustration_id'] = em_pred_df['illustration_id'].str[:-4]

merged_df = pd.merge(merged_df, clip_pred_df,  how='left', on=['illustration_id'])
merged_df = pd.merge(merged_df, em_pred_df,  how='left', on=['illustration_id'])

merged_df.to_csv("data/merged_all.csv", index=False)
