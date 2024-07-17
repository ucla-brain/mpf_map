## Transfer files

rsync -av --exclude '*/' user@remote:/path/to/source/folder/ /path/to/local/destination/

rsync -avh --exclude '*/' syamashi@clgui.bmap.ucla.edu:/panfs/dong/aspera/atlas_roigb/annotated_bw_atlas/ ~/Downloads/



## Generate orders

jq -R -s -c 'split("\n") | map(select(. != ""))' order.json > order2.json



## Delete images

  find /Users/seitayamashita/Downloads/mpfc_web_image_vis_for_seita -type f -name '*_15pct*' -exec rm {} +




## Find images


find /Users/seitayamashita/Downloads/mzhu_backups -type f -name "*.tif"

find /Users/seitayamashita/Downloads/mzhu_backups -type f -name "*.tif" | sed 's|/Users/seitayamashita/Downloads||g' > /Users/seitayamashita/Downloads/mzhu_backups_tiff_images.txt


while read -r keyword; do find /Users/seitayamashita/Downloads/mzhu_backups -name "*$keyword*" -print; done < ~/Desktop/dp_retro_cases.txt > ~/Desktop/dp_retrograde_resources.txt


awk -F '-' '{print $1 "-" $2}' ~/Desktop/dp_retro_cases.txt

while read -r keyword; do find /panfs/dong/aspera -name "*$keyword*" -print; done < ./dp_retrograde_cases.txt > ./dp_retrograde_resources.txt

