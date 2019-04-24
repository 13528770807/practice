#!/usr/bin/env bash

var=http://www.linuxidc.com/123.htm

echo ${var}

# 第一个下标为0
# echo ${var#*//}  # 删除"//"左边的字符
# echo ${var##*/}  # 删除(最右)"/"最后一个左边的字符
# echo ${var%/*}  #从右边开始，删除"/"右边的字符
# echo ${var%%/*}  # 从右边开始，删除(最左)"/"最后一个右边的字符

# echo ${var:7:3}  # 左边第几个字符开始，及截取字符的个数 www
# echo ${var:1:4}  # ttp:
# echo ${var:7:3}  # www
# echo ${var:0-11:3} # 从右向左边到11开始，截取三个字符 com
# echo ${var:0-3}


value1=home
value2=${value1}"="
echo $value2


