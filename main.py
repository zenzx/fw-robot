import sys
import json
import os

import sendEmail
import data

if __name__ == '__main__':
	if os.path.exists('./data.json') != True:
		print("您还没有配置您的邮箱\n")
		data.config()
	with open('./content.html', encoding='utf-8', mode='r') as f:
		contents = f.read()
	if sys.argv[1] == 'gmail':
		sendEmail.sender_mail(contents, sys.argv[1])
	elif sys.argv[1] == '163' or sys.argv[1] == 'qq':
		sendEmail.sender_mail(contents, sys.argv[1])
	else:
		# with open('./data.json', encoding='utf-8') as f:
		# 	data_dict = json.load(f)
		# if str(data_dict['user']['user_email']).find('qq')
		# TODO： 检查字典里面的账号属于什么服务器
		print("请选择你要使用的邮箱系统，目前支持QQ邮箱，网易邮箱，谷歌邮箱。")
		print("e.g. ..> python main gmail/qq/163")