import os
import json

def config():
	print("==============开始配置你的邮箱=============")
	user_name = input("请输入你的名字: ")
	user_email = input("请输入你的邮箱(支持QQ、网易、谷歌）：")
	user_passwd = input("请输入你的邮箱密码(应为SMTP码)：")
	receivers = input("请输入接受者的邮件(多个用户请使用逗号隔开):\n")
	receivers = receivers.split(",")
	data_dict = {
		'user':{
		'user_name': user_name,
		'user_email': user_email,
		'user_passwd': user_passwd,
		},
		'receivers': receivers,
	}
	with open('./data.json', 'w', encoding='utf-8') as f:
		json.dump(data_dict, f, ensure_ascii=False)
