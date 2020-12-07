from Transposition import *
from CifradoCesar import *
from SendEmail import *
from Socket import *
from Hunter import *
import argparse
import logging
import time
import os


logging.basicConfig(filename="Info.log", level="DEBUG")


parser = argparse.ArgumentParser(description=":::Description of the parameters:::")
# opc: options
parser.add_argument("-opc", type=int, 
	help="-opc (1=encode message, 2=unencode message, 3=hack encoded message, 4=Get Information of organizations, 5=Send Email, 6=Ckeck Ports)")
# if you want to encode/unencode/hack a message
# you have to choose between Cesar and Transposition
parser.add_argument("-t_cifr", type=int, help="-t_cifr (1=Cesar, 2=Transposition)")
# You have to definy the language of your message
parser.add_argument("-lang", type=int, help='-lang (1=English,2=Spanish)')
# msg: add your sentence
parser.add_argument("-msg", type=str, help='-msg "This is my message"')
# If you chose cesar, write the number of times you
# want to rot the letters
parser.add_argument("-rot", type=int, help='-rot (between 1 and 25)')
# If you chose transposition, write the string
parser.add_argument("-key", type=str, help="-key 'keyword'")
# If you want to use honter, add your api key and the domain
parser.add_argument("-apikey", type=str, help="-apikey '31mn93abbx811o05q119lDp1mms931ml5c31jjj7'")
parser.add_argument("-domain", type=str, help="-domain '(www.twitter.com / twitter.com / twitter)'")
# If you want to send a message, specify the type of
# email, it can be: 1=gmail, 2=outlook/hotmail
parser.add_argument("-t_email", type=int, help='-t_email (1=gmail, 2=hotmail/outlook)')
# Add your email and password to access to your email account
parser.add_argument("-email", type=str, help='-email "email@example.com"')
parser.add_argument("-passw", type=str, help='-pass "your_password"')
# Add the email where you want to send your message
parser.add_argument("-to", type=str, help='-to "email@example.com"')
# Add the subject for the email
parser.add_argument("-subj", type=str, help='-subj "subject"')
# If you want to send an image in your email, add this parameter
parser.add_argument("-pic", type=str, help='-pic "name_picture.jpg","c:\\users\\name\\pictures"')
# If you want to check the ip port, you would need the next parametrs
parser.add_argument("-ip", type=str, help='-ip "192.168.1.19"')
parser.add_argument("-port", type=int, help="-port 8080")
data = parser.parse_args()


#try:
if __name__ == '__main__':
	if(data.t_cifr == 1 or data.t_cifr == 2):
		# Cesar Cifrying
		if data.t_cifr == 1:
			# We call the ,odule where we have the principal code
			mold = CifradoCesar(data.opc, data.msg, data.rot)

			# if the user chose the cifrying option
			# we will enter to the next condicional
			if(data.opc == 1):
				print(":[*] Message encoded:", mold.codifyMessage())

			# This is the unencifrying option
			elif(data.opc == 2):
				print(":[*] Message unencoded:", mold.decodeMessage())

			# This is the hacking option
			elif(data.opc == 3):
				print(":[*] Message hacked:", mold.hackMessage())

		# Transposition Cifrying
		elif data.t_cifr == 2:
			t = Transposition()
			t.setLanguage(int(data.lang))
			t.setMessage(str(data.msg))

			try:
				if data.opc == 1:
					t.setKey(data.key)

					print(":[*] Message encoded:", t.encodeMessage())
					print()

				elif data.opc == 2:
					t.setKey(data.key)
					print(":[*] Message unencoded:", t.unencodeMessage())
					print()

				elif data.opc == 3:
					print(":[*] Message hacked:", t.hackMessage())
					print()

				elif opc == 4:
					pass
				else:
					logging.error("You chose an option does not exist", data.opc)
					print("[!] You added an invalid option")
					print("::: Closing program...")
			except:
				data.warning("You added an invalid message")
				print(":[!] You have added an invalid sentece / character.")
				print(":::: Closing program...")
				time.sleep(1)

	elif(data.t_cifr == None):
		# Use Honter with your api key
		if data.opc == 4:
			h = Hunter(data.apikey, data.domain)

			h.search()

			h.showInfo(h.search())
			h.saveInfo(h.search())

		elif data.opc == 5:
			se = SendEmail()

			t_email = data.t_email
			email = data.email
			password = data.passw
			to = data.to
			subject = data.subj
			se.setMessage(data.msg)
			msg = se.getMessage()


			part = ""
			if(t_email != None and email != None and password != None
				and to != None and subject != None and msg != None
				and data.pic != None):

				part = ""
				picture = ""
				directory = ""
				if((data.pic).count(",") == 1):
					data.pic = data.pic + ","
					for letter in data.pic:
						if letter != ",":
							part = part + letter

						elif letter == ",":
							if ".jpg" in part or ".jpeg" in part:
								picture = part
							else:
								directory = part
							part = ""

					se.setOpc(int(t_email))
					se.setEmailAccount(email)
					se.setPassword(password)
					se.setTo(to)
					se.setPictures(picture, directory)
					se.sendEmail(subject, msg)

				else:
					logging.warning("You have to add the name of your picture and its directory")
					print("[!] You can only add one picture and its directory")
					print("::: Closing program...")
					time.sleep(2)
					exit()

			elif(t_email != None and email != None and password != None
				and to != None and subject != None and msg != None
				and data.pic == None):

				se.setOpc(int(t_email))
				se.setEmailAccount(email)
				se.setPassword(password)
				se.setTo(to)
				se.sendEmail(subject, msg)

			else:
				logging.warning("You have to add more parameters")
				print("[!] We need more parameters to send the email")

		elif data.opc == 6:
			sckt = Socket()

			sckt.setIP(data.ip)
			sckt.checkPortSocket(data.port)

		elif data.opc == 7:
			directory = os.getcwd()
			os.system(f"powershell -ExecutionPolicy ByPass ./DNS.ps1 -TargetFolder \"{directory}\"")

		else:
			logging.warning("You have to add a valid optiion")
			print("[!] Error")
			print("::: Probably you did not add any option or")
			print("::: this one does not exist.")

	else:
		logging.error("This type of cifrying does not exist", str(data.t_cifr))
		print("[!] This type of cifrying does not exist")

#except:
#	logging.warning("Maybe you did not add a necesary/correct parameter")
#	print("[!] Error")
#	print("::: Maybe you did not add a necesary / correct")
#	print("::: parameter or you added a one invalid")