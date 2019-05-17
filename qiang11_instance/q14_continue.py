

num = int(input('请输入数字:'))
while num > 1:
    print('hello world')
    if num == 2:
        print('num2')
        continue  # 中断后重新开始
    else:
        print('num3')
        break
