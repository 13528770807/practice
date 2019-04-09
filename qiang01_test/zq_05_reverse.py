str="dhajdfna"
#问:用切片或其他方法对该字符串进行反转?


def reverse(str):
    ali = list()
    for l in str:
        ali.append(l)
    for i in range(len(ali)):
        if i <= len(ali)/2:
            ali[i-1], ali[-i] = ali[-i], ali[i-1]
    list_to_str = ''.join(ali)
    return list_to_str


if __name__ == "__main__":
    print(reverse(str))

















## str = input('请输入字符串')
#b = []
#for i in str:
#    b.insert(0, i)
#print(b)
#list_to_str = ''.join(b)
#print(list_to_str)
