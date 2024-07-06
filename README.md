# MPF Online Map

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

## Image conversions

1. Install conda environment
```
conda create --name utility
conda activate utility

conda install Pillow
conda install tqdm
```

2. Convert images to PNG file format

`% python convert_tiff_to_png.py /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita`

3. Resize PNG images

`% python resize_png_images.py /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita`

4. Copy images and dump a json file

`% python copy_and_dump_json.py /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita /Users/seitayamashita/Documents/git_next/mpf_map/static/images2`


```
python convert_tiff_to_png.py /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita
python resize_png_images.py /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita
python copy_and_dump_json.py /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita /Users/seitayamashita/Documents/git_next/mpf_map/static/images2
```