import pymysql as pymysql
a = None
user_data = {}
def mysql_db(name,age):
	conn = pymysql.connect(host='127.0.0.1', user='root', password='mysql', database='zhangqiang_db', charset='utf8')
	cursor = conn.cursor()
	sql = '''
	insert into USER1(name, age) value(%s, %s);
	'''
	# name = name
	# age = age
	cursor.execute(sql, [name, age])
	conn.commit()
	cursor.close()
	conn.close()


def serach_db(name):
	conn = pymysql.connect(host='127.0.0.1', user='root', password='mysql', database='zhangqiang_db', charset='utf8')
	cursor = conn.cursor()
	sql = '''
	select name from USER1 where name=%s;
	'''
	# name = name
	cursor.execute(sql, [name])
	a = cursor.fetchone()
	cursor.close()
	conn.close()
	print(a)
	return a

def serach_db_passwd(name):
	conn = pymysql.connect(host='127.0.0.1', user='root', password='mysql', database='zhangqiang_db', charset='utf8')
	cursor = conn.cursor()
	sql = '''
	select age from USER1 where age=%s;
	'''
	# name = name
	cursor.execute(sql, [name])
	passwd = cursor.fetchone()
	cursor.close()
	conn.close()
	print(passwd)
	return passwd

def new_user():
	name = input('new_name\t\n')
	while 1:

		if name in user_data:
			name = input('The user name already exists')
			continue
		else:
			break
	passwd = int(input('password\n'))
	mysql_db(name, passwd)
	# user_data[name] = passwd
	print('successful')


def old_user():

	name = input('name')
	while 1:
		username = serach_db(name)
		# print(serach_db(name))
		username = username[0]
		# print(a)

		# if name not in user_data:
		if username == name:
			print('name ok')
			password = input('password\n	')

			passwd = serach_db_passwd(password)
			passwd = str(passwd[0])
			if passwd == password:

				print('登录成功')


			name = input('name is error,please enter again')
			continue
		else:
			break
	pwd= user_data.get(name)
	if passwd == pwd:
		print('successful')
		
	else:
		print('password is error')
def showmenu():
	name = ''
	print('---new_user:N/n--')
	print('---login:E/e------')
	print('---quit:Q/q------')
	print('---input code----')
	choose=input('input code\n')	
	while 1 :
		if choose not in 'NEQneq':
			choose = input('code is error,try again')
		elif choose == 'q' or choose == 'Q':
			break
		elif  choose == 'N' or choose =='n':
			new_user()
			showmenu()
		elif  choose =='e' or choose == 'E':
			old_user()
showmenu()
# if serach_db('laowang') == ('laowang',):
# 	print('1')
# else:
# 	print('2')
#


		
