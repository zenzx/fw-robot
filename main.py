import email
import sys

import sendEmail

if __name__ == '__main__':
	if sys.argv[1] == 'gmail':
		sendEmail.sender_mail("<h1>FwRot</h1>")