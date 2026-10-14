#!/bin/bash

wth=`file $1 | grep -o '[0-9]* *x' | grep -o '[0-9]*'`
hgt=`file $1 | grep -o 'x *[0-9]*' | grep -o '[0-9]*'`

sortings/$3 $wth $hgt

cmd.exe /c python __main__.py $1 $2

#rm sequence.txt