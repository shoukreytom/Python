import smtplib, ssl


def main():
	sender = "shoukreytom01@gmail.com"
	reciever = "researchersci@gmail.com"
	message = """From: %s
	To: %s
	Subject: Testing
	this is a test for sending mails using python
	"""%(sender, reciever)
	try:
		password = input("Enter your password")
		smp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		smp.login(sender, password)
		smp.sendmail(sender, reciever, message)
		print("mail sent successfully")
	except:
		print("Something went wrong")


if __name__ == '__main__':
	main()
