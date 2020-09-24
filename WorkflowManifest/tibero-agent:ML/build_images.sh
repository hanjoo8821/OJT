#!/bin/bash -e

# --------------------------------------------
dir1=01-TiberoAgent

image_name1=hanjoo8821/jdbc-tibero
image_tag1=colsout-0.2
full_image_name1=${image_name1}:${image_tag1}

cd "$(dirname "$0")/${dir1}"
docker build -t "${full_image_name1}" .
docker push "$full_image_name1"

# --------------------------------------------
dir2=02-1-Trans

image_name2=hanjoo8821/jdbc-tibero
image_tag2=trans-emp-0.2
full_image_name2=${image_name2}:${image_tag2}

cd ..
cd "$(dirname "$0")/${dir2}"
docker build -t "${full_image_name2}" .
docker push "$full_image_name2"

# --------------------------------------------
dir3=02-2-Trans

image_name3=hanjoo8821/jdbc-tibero
image_tag3=trans-birth-0.2
full_image_name3=${image_name3}:${image_tag3}

cd ..
cd "$(dirname "$0")/${dir3}"
docker build -t "${full_image_name3}" .
docker push "$full_image_name3"

# --------------------------------------------
cd ..
python pipeline.py