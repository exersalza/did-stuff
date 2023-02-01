#!/bin/bash

if [ "$EUID" -ne 0 ]
then
  echo "Please run with sudo."
  exit 2
fi

echo "Running update..."
cp -pr ./templates/* /usr/share/salty-create
cp -p main.py /usr/bin/salty-create
echo "Updated"