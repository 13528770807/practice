#ali = list()
#small_list = []
##num = 15
#fac = 1
#for num in range(1, 17):
#    while fac <= num:
#        if num % fac == 0:
#            ali.append(fac)
#        # for i in ali:
#        #     if fac == num:
#        #         small_list.append(ali[:num])
#        fac += 1
#    fac = 1
#    # print(ali)
#adic = {}
#for i in range(len(ali)):
#    adic[i] = ali[i]
#
#a = 0
#for k, y in adic.items():
#    # print("%s:%s" % (k, y))
#    if y == 1:
#        # k = 1
#        # print(ali[a:k])
#        small_list.append(ali[a:k])
#        # print(small_list)
#        a = k
#small_list.pop(0)
## print(small_list)
#for l in small_list:
#    print(l)
#
#
## print(adic)
## print(ali[0:1])
## print(ali[1:3])
## print(ali[3:5])
## print(ali[5:8])
## print(ali[8:10])
#


ali = list()
small_list = []
adic = {}


def factors(star, end, fac=1, a=0):
    for num in range(star, end+2):
        while fac <= num:
            if num % fac == 0:
                ali.append(fac)
            fac += 1
        fac = 1

    for i in range(len(ali)):
        adic[i] = ali[i]

    for k, y in adic.items():
        if y == 1:
            small_list.append(ali[a:k])
            a = k

    small_list.pop(0)
    for l in small_list:
        print(l)


if __name__ == "__main__":
    factors(1, 15)

