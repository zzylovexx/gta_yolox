#!/bin/bash

for file in gtadataset/test/* #select which directory i wnat to recursive
do 
    echo ${file}
    python tools/demo.py  --path ${file} 
done
