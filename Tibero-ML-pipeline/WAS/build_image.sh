#!/bin/bash -e

ver=1.0

# --------------------------------------------
image_name=hanjoo8821/was-flask
image_tag=ml
full_image_name=${image_name}:${image_tag}-${ver}

cd "$(dirname "$0")"
docker build -t "${full_image_name}" .
docker push "$full_image_name"