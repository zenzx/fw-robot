import sendEmail

if __name__ == '__main__':
	with open('./content.html', encoding='utf-8', mode='r') as f:
		contents = f.read()
	sendEmail.sender_mail(contents)
