from email.message import EmailMessage
import Message
import smtplib
import getpass
import imghdr
import time
import ssl
import re
import os


class SendEmail(Message.Message):

	def __init__(self):
		super().__init__()
		self.email_account = ""
		self.password = ""
		self.opc = 0
		self.pictures = []
		self.to = ""


	###################################################################
	def setOpc(self, opc):
		if opc == 1 or opc == 2:
			self.opc = opc

		elif opc == 3:
			print(":[*] Closing program...")
			time.sleep(2)
			exit()

		else:
			print(":[!] This option does not exist")

	def getOpc(self):
		return self.opc


	####################################################################
	def setEmailAccount(self, email_account):
		# If the user chose to add a gmail email,
		# we enter to the first conditional
		if self.getOpc() == 1:

			# There are some character that can't be accepted for
			# a gmail account
			cant_be = "|°¬!\"$%&/()='?\\¿¡´¨+*~{[^}]`,;:-_<>éýúíóáÉÝÚÍÓÁëÿüïöäËÜÏÖÄ"

			# We use this 'for' to check each character
			# in the variable called cant_be
			for character in cant_be:

				# We use the next conditional to verify
				# if the character or an space is in the
				# email our user added
				if character in email_account or " " in email_account:

					email_account = ""

					# If enter to the condition, we request the
					# email again 
					print(":[!] Invalid character")

			# Now we use a regular expression to be sure
			# our user used '@' and the domain of gmail 
			type_email = re.match(r"(.*?)@gmail.com", email_account)

			# Verify the regular expression
			if type_email:
				# If the regular expression found a valid
				# email, we saved it in 'self.email_account'
				self.email_account = type_email[0]

		############################################
		# If the user chose to send an email from an 
		# outlook/hotmail account, we enter to this
		# conditional
		elif self.getOpc() == 2:

			# There are character can´t be in an outlook/hotmail
			# account, so, we saved these in 'cant_be'
			cant_be = "|°¬!\"$%&/()='?\\¿¡´¨+*~{[^}]`,;:<>éýúíóáÉÝÚÍÓÁëÿüïöäËÜÏÖÄ"

			# We use this 'for' to check each character
			# in the variable called cant_be
			for character in cant_be:

				# We use the next conditional to verify
				# if the character or an space is in the
				# email our user added
				if character in email_account or " " in email_account:

					email_account = ""

					# If enter to the condition, we request the
					# email again 
					print(":[!] Invalid character")

			# Outlook accept two emails type, outlook.com
			# and hotmail.com, so, in the next list we add 
			# a regular expression to each type of email
			type_emails = [re.match(r"(.*?)@(outlook.es|outlook.com|uanl.edu.mx)", email_account), re.match(r"(.*?)@hotmail.com", email_account)]

			# We use the next 'for' to use each regular
			# expression 
			for type_email in type_emails:

				# If one of the regular expressions is okay,
				# we enter to this conditional
				if type_email:

					# We save the email in 'self.email_account' 
					self.email_account = type_email[0]

		if self.email_account == "":
			email_account = ""
			print(":[!] You didn't add a valid email")

	def getEmailAccount(self):
		return self.email_account


	def setPassword(self, password):
		if "@gmail.com" in self.email_account:
			# Gmail only request the password length 
			# to be longer than 7
			if len(password) >= 8:
				self.password = password

		else:
			# Gmail request the password length 
			# to be longer than 7 and...
			if len(password) >= 8:

				# The password has to content two different
				# characters type (one capitalize letter and 
				#                  one number,...).
				# So, we saved different characters in diffe-
				# rents variables
				cap = "ABDEFGHIJKLMNÑOPQRSTUVWXYZ"
				lower = "abdefghijklmnñopqrstuvwxyz"
				numbers = "0123456789"
				symbols = "|°¬!\"$%&/()='?\\¿¡´¨+*~{[^}]`,;:-_<>éýúíóáÉÝÚÍÓÁëÿüïöäËÜÏÖÄ"

				# We use counters to count how many characters
				# type are in the password
				c_cap = 0
				c_lower = 0
				c_numbers = 0
				c_symbols = 0
				counter = 0

				# We use some 'for' for the before mentioned
				for i in cap:
					if i in password:
						c_cap = c_cap + 1

				for j in lower:
					if j in password:
						c_lower = c_lower + 1

				for k in numbers:
					if k in password:
						c_numbers = c_numbers + 1

				for l in symbols:
					if l in password:
						c_symbols = c_symbols + 1

				# We use the next condicionals and a counter to 
				# count how many counters have longer than 0
				if c_cap > 0:
					counter = counter + 1

				if c_lower > 0:
					counter = counter + 1

				if c_numbers > 0:
					counter = counter + 1

				if c_symbols > 0:
					counter = counter + 1

				# If the counter length is longer than 1,
				# the password satisfie an outlook/hotmail
				# password, so...
				if counter >= 2:

					# We save this one in 'self.password'
					self.password = password

		# We use the next condicional to verify if
		# 'self.password' is empty, because it
		# means the user added an invalid password, so...
		if self.password == "":

			# We empty password and...
			password = ""

			# Request this one again
			print(":[!] You added an invalid password")

	def getPassword(self):
		return self.password


	#######################################################################
	def setTo(self, to):
		if " " not in to:
			# Now we use a regular expression to be sure
			# our user used '@' and the domain of gmail 
			type_email = re.search(r"(.*?)@(.*?)", to)

			# Verify the regular expression
			if type_email:
				# If the regular expression found a valid
				# email, we saved it in 'self.email_account'
				self.to = to

			else:
				to = ""
				print(":[!] You added an invalid email")

		else:
			to = ""
			print(":[!] You added an invalid email")

	def getTo(self):
		return self.to


	######################################################################
	def setPictures(self, image, directory):
		pictures = []

		if '.jpeg' in image:
			image = image.replace(".jpeg", "jpg")

		verify_image = re.search(r'\w*.jpg', image)
		if verify_image:
			directory = directory.lower()
			print()

			if "c:\\" in directory:
				pictures.append(image)
				pictures.append(directory)
				self.pictures = pictures

		else:
			print(":[!] This is not an image")

	def getPictures(self):
	       return self.pictures


	#####################################################################
	def sendEmail(self, subject, msg):
		message = EmailMessage()
		message["Subject"] = subject
		message["From"] = self.email_account
		message["To"] = self.to
		message.set_content(msg)

		if len(self.pictures) > 0:
			try:
				if self.pictures[1] == os.getcwd().lower():
					os.chdir("c:\\")
				os.chdir(self.pictures[1])

				file = open(self.pictures[0], 'rb')
				f_name = file.name
				f_data = file.read()
				f_type = imghdr.what(file.name)
				file.close()

				message.add_attachment(f_data, maintype='image', subtype=f_type, filename=f_name)
			except:
				print(":[!] The directory / image you added does not exist or")
				print(":::: this one is not in the directory.")
				exit()

		try:
			if self.opc == 1:
				server = smtplib.SMTP("smtp.gmail.com", 587)

			elif self.opc == 2:
				server = smtplib.SMTP("smtp-mail.outlook.com", 587)

			server.starttls(context=ssl.create_default_context())
			server.login(self.email_account, self.password)
			server.send_message(message)
			server.quit()

			print("[*] Email sended")
		except:
			print(":[!] You haven't habilited the less")
			print(":[!] secure apps in your account.")
			print(":[!] Closing program...")
			time.sleep(2)
			exit()