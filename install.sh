#!/bin/bash

if [ "$EUID" -ne 0 ]
then
  echo "Please run with sudo."
  exit 2
fi

echo "Creating Dirs"
mkdir /usr/share/salty-create/

echo "Copying Templates"
cp -pr ./templates/* /usr/share/salty-create

echo "Creating executable"

cp -p main.py /usr/bin/salty-create