#!/bin/bash -e

ver=1.0

# --------------------------------------------
dir1=01-TiberoAgent

image_name1=hanjoo8821/jdbc-tibero
image_tag1=colsout
full_image_name1=${image_name1}:${image_tag1}-${ver}

cd "$(dirname "$0")/${dir1}"
docker build -t "${full_image_name1}" .
docker push "$full_image_name1"

# --------------------------------------------
dir2=02-1-Trans

image_name2=hanjoo8821/jdbc-tibero
image_tag2=trans-salary
full_image_name2=${image_name2}:${image_tag2}-${ver}

cd ..
cd "$(dirname "$0")/${dir2}"
docker build -t "${full_image_name2}" .
docker push "$full_image_name2"

# --------------------------------------------
dir3=02-2-Trans

image_name3=hanjoo8821/jdbc-tibero
image_tag3=trans-birth
full_image_name3=${image_name3}:${image_tag3}-${ver}

cd ..
cd "$(dirname "$0")/${dir3}"
docker build -t "${full_image_name3}" .
docker push "$full_image_name3"

# --------------------------------------------
dir4=03-ML

image_name4=hanjoo8821/jdbc-tibero
image_tag4=ml
full_image_name4=${image_name4}:${image_tag4}-${ver}

cd ..
cd "$(dirname "$0")/${dir4}"
docker build -t "${full_image_name4}" .
docker push "$full_image_name4"

# --------------------------------------------
dir5=04-Visualize

image_name5=hanjoo8821/jdbc-tibero
image_tag5=graph
full_image_name5=${image_name5}:${image_tag5}-${ver}

cd ..
cd "$(dirname "$0")/${dir5}"
docker build -t "${full_image_name5}" .
docker push "$full_image_name5"

# --------------------------------------------
cd ..
python pipeline.py