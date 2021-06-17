import email
import sys

import sendEmail

if __name__ == '__main__':
	with open('./content.html', encoding='utf-8', mode='r') as f:
		contents = f.read()
	if sys.argv[1] == 'gmail':
		sendEmail.sender_mail("<h1>FwRebot</h1>")
	elif sys.argv[1] == '163' or sys.argv[1] == 'qq':
		sendEmail.sender_mail("<h1>FwRebot</h1>")
	else:
		print("请选择你要使用的邮箱系统，目前支持QQ邮箱，网易邮箱，谷歌邮箱。")
		print("e.g. ..> python main gmail/qq/163")