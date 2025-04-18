# MPF Online Map

A single-page application for visualizing the projection patterns of anterograde and retrograde tracing in the MPF.

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
python overlay_images.py /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita /Users/seitayamashita/Downloads/annotated_bw_atlas
python copy_and_dump_json.py /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita /Users/seitayamashita/Documents/git_next/mpf_map/static/images
```

on Panfs
```
python convert_tiff_to_png.py /panfs/dong/mpf_map/output
python resize_png_images.py /panfs/dong/mpf_map/output
python overlay_images.py /panfs/dong/mpf_map/output /panfs/dong/mpf_map/annotated_bw_atlas
```
And copied the images over locally to see if the changes are reflected.


5. ARA images

```
python convert_tiff_to_png.py /Users/seitayamashita/Downloads/annotated_bw_atlas
python resize_png_images.py /Users/seitayamashita/Downloads/annotated_bw_atlas 
#python copy_and_dump_json.py /Users/seitayamashita/Downloads/annotated_bw_atlas /Users/seitayamashita/Documents/git_next/mpf_map/static/ara
```

## Exceptional image which contains a border line and how to remove it


1. Remove a border line
 `% python remove_black_border.py /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita/SW120403-02A-ACAv/2-phal/SW120403-02A_2_10_ch2_ACAv_phal_ara075.tif /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita/SW120403-02A-ACAv/2-phal/SW120403-02A_2_10_ch2_ACAv_phal_ara075.tif`

2. Convert a TIFF image to PNG file format 
`% python convert_tiff_to_png.py -i /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita/SW120403-02A-ACAv/2-phal/SW120403-02A_2_10_ch2_ACAv_phal_ara075.tif -o /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita/SW120403-02A-ACAv/2-phal/SW120403-02A_2_10_ch2_ACAv_phal_ara075.png`

3. Resize PNG image
4. Copy images and dump a json file


## Retrograde images and regenerate cell segmentations from degeneraged images

Retrograde images depends on the cell size of the cell center.  The degenerated images provided are too small for visualization.  Run the following script to regenerate retrograde images with larger pixel size.

1. Create a conda environment to use Outspector.

```
conda create -f /ifshome/syamashi/Documents/gittest/outspector/src/grid_env/conda_grid.yml 
```

```
% python batch_cell_segmentation.py /panfs/dong/mpf_map/originals/ /panfs/dong/mpf_map/output/
```


## Ontology

List of anterograde injections and retrograde injections.

Anterograde:
```
SW110614-01B-ACAd/2-phal
SW170420-03A-ACAd/4-aav-rfp
SW170420-04A-ACAd/4-aav-rfp
SW110321-04B-ACAv/2-phal
SW110606-01A-ACAv/2-phal
SW120403-02A-ACAv/2-phal
SW151027-02B-DP/2-phal
SW160120-01B-DP/2-phal
SW160120-03A-DP/2-phal
SW160120-03A-DP/4-aav-rfp
SW170420-03A-DP_deep/2-phal
SW170420-04A-DP_deep/2-phal
SW120404-01A-ILA/2-phal
SW120404-02A-ILA/2-phal
SW120404-04A-ILA/2-phal
SW110613-02B-PL/2-phal
SW110808-04A-PL/2-phal
SW120530-03A-PL/2-phal
```

Retrograde:
```
SW110614-01B-ACAd/5-ctb
SW120530-03A-ACAd/3-fg
SW170420-04A-ACAd/3-fg
SW110321-04B-ACAv/5-ctb
SW110606-01A-ACAv/5-ctb
SW120403-02A-ACAv/5-ctb
SW151027-02B-DP/4-ctb
SW160120-01B-DP/5-ctb
SW160120-03A-DP/5-ctb
SW170420-04A-DP_deep/5-ctb
SW120404-02A-ILA/5-ctb
SW120404-04A-ILA/5-ctb
SW120404-01A-PL/3-fg
SW120404-02A-PL/3-fg
```

Note:
```
DP is DPs
deep is DPd
```

## Color codes for image tinting

```
ILA: 56, 127, 185
PL: 255, 127, 0
DPs: 228, 26, 28
DPd: 76, 175, 74
ACAd: 166, 86, 41
ACAv: 152, 79, 163
```

## Shadow mask on ARA

For not available ARA levels, place holder images are needed.  Create masked shadow images from ARA images.

```
python apply_shadow_mask.py /Users/seitayamashita/Documents/git_next/mpf_map/static/ara
```

## Image Menu GUI json

You would need to run this to update the `imageMenu.json` used in the `ImageMenu.vue`.

```
python generate_image_menu_gui_data.py /Users/seitayamashita/Documents/git_next/mpf_map/static/images/orders.json /Users/seitayamashita/Documents/git_next/mpf_map/src/assets/
```

----

## Docker

0. Build

```
% npm run build
```

1. Start Docker container
```
% docker-compose down -v
% docker-compose up --build -d
```

2. Access http://localhost:8082/

3. Password protection (optional)

```
htpasswd -c ./nginx/.htpasswd guest
```

## Contributors
- Seita Yamashita

[![UCLA B.R.A.I.N.](https://uclabrain.org/wp-content/uploads/2024/12/logo-9-a2small.png)](http://brain.neurobio.ucla.edu/)

[UCLA B.R.A.I.N.](http://brain.neurobio.ucla.edu/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

