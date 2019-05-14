

for i in range(1001):
    n = len(str(i))
    # print(n)
    # if (i % 10)**n == i:
    if ((i % 10)**n) + (((i//10) % 10)**n) + (((i//100) % 10)**n) == i:
        print(i)


for i in range(1001):
    if (i % 10)**3 + ((i//10) % 10)**3 + ((i//100) % 10)**3 == i:
        # print(i)
        pass


print("="*60)
num = int(input('请输入一个数:'))
n = len(str(num))
print(n)

sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    # print('digit', digit)
    sum += digit ** n
    # print('sum:', sum)
    temp //= 10
    # print('temp:', temp)

if num == sum:
    print(num, '是阿姆斯特朗数')
else:
    print(num, '不是阿姆斯特朗数')


