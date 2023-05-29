from glob import glob


tif_files = glob('data/all_images/early_modern_images/tif_rgba/*.TIF')
png_files = glob('data/all_images/early_modern_images/png_final/*.png')

def get_ext_stripped_files(files):
    stripped = [f.split('.')[0].split('/')[-1] for f in files]
    return stripped

tif_stripped = get_ext_stripped_files(tif_files)
png_stripped = get_ext_stripped_files(png_files)

png_missing = list(set(tif_stripped) - set(png_stripped))

# Result:
# All the missing images (~100) are corrupt images that that could not be opened.
