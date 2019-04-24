#!/usr/bin/env bash
# 第一类：数字性循环
for((i=6;i<=10;i++));
do
    num=$(expr $i \* 2)
    echo $num
done

for i in $(seq 1 10)
do
    echo `expr $i \* 2`
done

for i in {1..10}
do
    echo $i
done
echo '=============='
# awk 'BEGIN{for(i=1;1<=10;i++) print i}'

# 第二类：字符性循环
for i in `ls`;
do
    echo $i is file name\!
done
echo '-------------'
for i in $* ;
do
    echo $i is input chart\!
done

echo '------------------'
for i in f1 f2 f3 ;
do
    echo $i in appoint ;
done

echo '----------------------------'
list="rootfs usr data data2"
for i in $list;
do
echo $i is appoint ;
done

# list="rootfs usr data data2"
# for i in $list;
# do
# echo $i is appoint ;
# done

echo '-----------------------------'


# 第三类：路径查找
for i in /home/dev/PycharmProjects/practice/qiang02_shell/photo090/* ;
do
    echo $i
done

# for file in /proc/*;
# do
# echo $file is file path \! ;
# done

echo '--------------------'

for i in $(ls *.sh)
do
    echo $i
done

echo '----------------------------'


