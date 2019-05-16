

with open('test_io.txt', 'w') as out_file:
    out_file.write('这里是输入的文字\nhello world')


with open('test_io.txt', 'r') as in_file:
    txt = in_file.read()
    print(txt)