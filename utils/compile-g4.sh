#!/bin/bash

foldername=$(basename $1)
#foldername="${1##*/}"
cd $1
cd ..
folder="build-$foldername"

if [ ! -d "$folder" ]; then 
	mkdir $folder
fi
cd $folder
source /opt/geant4.10.01.p03/bin/geant4.sh
cmake -DGeant4_DIR=/opt/geant4.10.01.p03 $1
make -j4



