import sys
print("\n\npython路经为:", sys.path, '\n')  # \n 换行

print('命令行参数如下：')
for i in sys.argv:
    print(i)