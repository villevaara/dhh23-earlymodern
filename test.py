import pandas as pd


captions_df = pd.read_csv("data/illustration_captions.csv",
                          dtype={"ecco_id": str, "page_id": str})

orig_sample = pd.read_csv("data/random_sample.csv",
                          dtype={"ecco_id": str, "page_id": str})

meta_sample = pd.read_csv("data/metadata_sample.csv",
                          dtype={"ecco_id": str, "page_id": str})


all_sci = pd.read_csv("data/ecco_sci_urls.csv",
                    dtype={"ecco_id": str, "page_id": str})

