#!/usr/bin/env bash
echo 'helloa'

test -d qiang_02_shell

echo $?

# for A in `ls`
for A in $(ls)
do
    test -d $A
    if [ $? -eq 0 ]
    then
        echo diretor is $A
    else
        echo file is $A
    fi
done
echo `ls`
echo '============'


name=zhangqiang
firstname=${name#*g}
lastname=${name%q*}
echo ${firstname}
echo ${lastname}
echo ${lastname}${firstname}

mv ${name} ${firstname}${lastname}
echo ${name}


