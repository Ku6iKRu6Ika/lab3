#!/bin/bash

for file in *.c; do
	if [ "$file" == "saver.c" ]; then
		continue
	fi
	name=${file%.*}
	g++ saver.c $file -o $name
done
