#!/usr/bin/env bash


 for num in $(seq 1 10)
 do
     nums=$(expr $num \* 2)
     echo $nums
 done

echo '=================================='

for pic in `ls photo090 | grep .jpg`
do
    # echo ${pic}
    # names=${pic#*-}
    # echo ${names}
    # mv ${pic} ${names}

    newfile=`echo $pic | sed s/my/$num/g`
    # mv $pic $newfile

    # newfile=`echo $pic | sed 's/\([a-z]\+\)_\([a-z]\+.*\)/\1_-0.4845.jpg/'`
    # newfile=`echo $pic | sed 's/\([a-z]\+\)_\([a-z]\+.*\)/\1_-0.483.jpg/'`
    # todo .*
    # newfile=`echo $pic | sed 's/\([a-z]\+\)_\([a-z]\+.*\)/\$nums_-0.4834.jpeg/'`
    echo $newfile

    # touch ./file_name/$newfile
    # mv ./photo09/$pic ./photo09/$newfile
    # echo ${#pic}

done

# c09用的x偏移为：-0.4845
# c12用的x偏移为：-0.483

# 是否检查出车牌/是否通行/是否遮挡