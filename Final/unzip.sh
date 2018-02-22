#!/bin/bash

for i in $(ls -1 *.bz2 | grep -i student); do
    file=$i
    num=$(echo $i | sed -r 's/[Ss]tudent([0-9]{1,2}).*/\1/g')
    if [[ $num  =~ ^0.* ]]; then
        num=$(echo $num | sed -r 's/0(.*)/\1/g')
    fi

    mkdir student$num 2>/dev/null
    mv $i student${num}/
done

for i in $(ls -d1 student*); do
    cd $i
    tar xf *.bz2
    cd ..
done

find ./ -type f -regex ".*[Ff]inal.exam.txt"
    
