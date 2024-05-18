#! /bin/bash

acr_id="flipkartscrapper.azurecr.io"
image_name="flipkartscrapper"
docker login "$acr_id"
docker build --tag "$acr_id/$image_name" .
docker push "$acr_id/$image_name:latest"