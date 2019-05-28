

# sed 【options】  ‘【command】’ 【filename】
"""
vim sed.txt

12345
23456
34567
45678
56789
67890
78901

sed -i 's/6/zqiang/g' ./sed.txt  # 替换
12345
2345zqiang
345zqiang7
45zqiang78
5zqiang789
zqiang7890
78901

sed -n 3p sed.txt  # 对第三行进行操作 p打印出
345zqiang7

sed -n '1,3p' sed.txt  # 显示1-3行的内容
12345
2345zqiang
345zqiang7

sed -n '1,3!p' sed.txt  # 加感叹号就是除了1-3显示其他所有内容
45zqiang78
5zqiang789
zqiang7890
78901

sed -n '3,+3p' sed.txt  # 显示第三行和之后的三行
345zqiang7
45zqiang78
5zqiang789
zqiang7890


sed '1i###' sed.txt  在文件的头插入“###”
###  #这个改完之后是不保存的 ，原文件还是老样子
12345
2345zqiang
345zqiang7
45zqiang78
5zqiang789
zqiang7890
78901

sed '1i###' sed.txt > a.txt  # 重定向
###
12345
2345zqiang
345zqiang7
45zqiang78
5zqiang789
zqiang7890
78901

sed '1i###' sed.txt >> a.txt  # 追加
###
12345
2345zqiang
345zqiang7
45zqiang78
5zqiang789
zqiang7890
78901

###
12345
2345zqiang
345zqiang7
45zqiang78
5zqiang789
zqiang7890
78901

sed '$a@@@' sed.txt >> a.txt  # 在文件尾部追加@@@   $代表尾部a代表追加
12345
2345zqiang
345zqiang7
45zqiang78
5zqiang789
zqiang7890
78901

@@@

sed '3c$$$' sed.txt  # 第三行插入$$$ (替换)
12345
2345zqiang
$$$
45zqiang78
5zqiang789
zqiang7890
78901
"""

# awk
"""
vim result.txt
aa 7 17 27 37 47 57
bb 8 18 28 38 48 58
cc 9 19 29 39 49 59
dd 6 16 26 36 46 56

awk '{print $0}' result.txt  # $0显示所有内容 (单引号)
aa 7 17 27 37 47 57
bb 8 18 28 38 48 58
cc 9 19 29 39 49 59
dd 6 16 26 36 46 56

awk '{print $1}' result.txt  # $1显示内容的第一列
aa
bb
cc
dd

vim sed.txt 
123:4,5
234:5,zqiang
345:z,qiang7
45z:q,iang78
5zq:i,ang789
zqi:a,ng7890
789:0,1

awk -F: '{print $1}' sed.txt  # 显示 reuslt.txt 第一列，以：作为分隔符
123
234
345
45z
5zq
zqi
789

awk '{print $1,$5}' result.txt   # 显示第一列和第五列内容
aa 37
bb 38
cc 39
dd 36

awk 'BEGIN{print "start search result.txt"}{print $1,$2,$3}END{print "end of result.txt"}' result.txt
# 这更有点儿python嵌套的意思了，也不是给取的值 取个名字，也不是嵌套就是给要取的值赋了个名字
start search result.txt
aa 7 17
bb 8 18
cc 9 19
dd 6 16
end of result.txt

awk '$2 >= 8 {print $0}' result.txt  # 查询第二列大于等于8的 符合条件的所有值列出来
bb 8 18 28 38 48 58
cc 9 19 29 39 49 59

awk '{if($1=="bb" || $2=="9") print $0}' result.txt  # 查询第一列等于"bb",第二列等于"9" 符合条件的所有值列出来
bb 8 18 28 38 48 58
cc 9 19 29 39 49 59

"""
