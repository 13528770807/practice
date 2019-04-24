#!/usr/bin/env bash

for pic in `ls photo09`
do
    echo ${pic}
    names=${pic#*-}
    echo ${names}
    mv ${pic} ${names}

done



#for file in `ls ../qiang03_testshell `
#
#do
#    echo ${file}
#    fname=${file:0:3}
#    bname=${file:4}
#    iname=${file:3:1}
#    lname=${bname}${iname}${fname}
#    echo ${lname}
#    mv ${file} ${lname}
#done