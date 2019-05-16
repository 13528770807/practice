

str = 'hello world'
# 判断字符串
print(str.islower())  # 判断所有字符小写
print(str.isupper())  # 判断所有字符大写
print(str.istitle())  # 判断所有字符首字母大写,像标题
print(str.isalpha())  # 判断所有的字符都是字母
print(str.isdigit())  # 判断所有字符都是数字
print(str.isalnum())  # 判断所有字符都是字母和数字
print(str.isspace())  # 判断所有字符都是空白字符, \t \n \r
print(str)

print('='*60)

# 字符串转换
print(str.upper())  # 将所有字符小写字母转为大写字母
print(str.lower())  # 将所有字符大写字母转为小写字母
print(str.title())  # 将所有单词首字母转为大写, 其余小写
print(str.capitalize())  # 将第一个单词首字母转为大写, 其余小写