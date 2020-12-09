import Message
import time

class CifradoCesar(Message.Message):
	def __init__(self, mode, message, key):
		super().__init__()
		self.mode = mode
		self.verifyMode()

		super().setMessage(message)
		self.message = super().getMessage()

		self.key = key
		self.verifyKey()

	#######################################################
	def verifyMode(self):
		mode = self.mode
		if(mode == None):
			print("[!] You did not add the '-mode' parameter")
			exit()
		elif(mode < 1 or mode > 3):
			print("[!] The mode '" + str(mode) + "' does not exist.")
			exit()
		else:
			print("[*] Valid mode")
			return mode

	def verifyKey(self):
		key = self.key
		if(self.mode == 1 or self.mode == 2):
			if(key == None):
				print("[!] You did not add the '-key' parameter")
				exit()
			elif(key < 1 or key > 25):
				print("[!] The key '" + str(key) + "' does not exist.")
				exit()
			else:
				print("[*] Valid Key")
				key = key
				return key

		elif(self.mode == 3):
			# If the user add the key parameter, we send an advertence
			# because we do not need it one
			if(key != None):
				print("[!] You do not have to add a key to hack")
				print("::: the message")
				exit()
			
			elif(key == None):
				return True


	############################################################
	def codifyMessage(self):
		for i in range(1, 3, 1):
			super().setLanguage(i)
			average = super().verifyLanguage(self.message)

			if(average >= 50):
				alphabet = "abcdefghijklmnopqrstuvwxyz"
				msg = super().getMessage().lower()
				message = msg.replace("ñ", "n")

				key = self.key
				codify_message = ""
				cont = 0

				for letter in message:
					if(letter not in alphabet):
						codify_message = codify_message + letter
					else:
						for letter2 in alphabet:
							if(letter == letter2):
								j = cont + key
								if j > 25:
									j = j - 26
								codify_message = codify_message + alphabet[j]
							cont = cont + 1
						cont = 0				
				return codify_message
				break

		if(average < 50):
			print("[!] Your messsage was not encoded.")
			print("::: We only accept english / spanish, maybe")
			print("::: the original message was wrote in a di-")
			print("::: fferent language.")
			time.sleep(1)
			exit()


	def decodeMessage(self):
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		msg = super().getMessage().lower()
		message = msg.replace("ñ", "n")

		key = self.key
		decode_message = ""
		cont = 0

		for letter in message:
			if(letter not in alphabet):
				decode_message = decode_message + letter
			else:
				for letter2 in alphabet:
					if(letter == letter2):
						j = cont - key
						if j > 25:
							j = j - 26
						decode_message = decode_message + alphabet[j]
					cont = cont + 1
				cont = 0

		aux = False
		# Verify language
		for i in range(1, 3, 1):
			super().setLanguage(i)

			average = super().verifyLanguage(decode_message)
			if(average >= 30):
				aux = True
				return decode_message
				break
			else:
				continue

		if aux == False:
			print("[!] Your messsage was not unencoded.")
			print("::: We only accept english / spanish, maybe")
			print("::: the original message was wrote in a di-")
			print("::: fferent language.")
			time.sleep(1)
			exit()


	#####################################################
	def hackMessage(self):
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		msg = super().getMessage().lower()
		message = msg.replace("ñ", "n")

		for key in range(0, 26, 1):
			decode_message = ""
			cont = 0

			for letter in message:
				if(letter not in alphabet):
					decode_message = decode_message + letter
				else:
					for letter2 in alphabet:
						if(letter == letter2):
							j = cont - key
							if j > 25:
								j = j - 26
							decode_message = decode_message + alphabet[j]
						cont = cont + 1
					cont = 0

			aux = False
			# Verify language
			for i in range(1, 3, 1):
				super().setLanguage(i)

				average = super().verifyLanguage(decode_message)
				if(average >= 30):
					aux = True
					#return decode_message
					break
				else:
					continue

			if aux == True:
				break

		if aux == True:
			return decode_message

		elif aux == False:
			print("[!] We are sorry, we can not hack the message.")
			print("::: We only accept english / spanish, maybe the")
			print("::: original message was wrote in a different")
			print("::: language.")
			time.sleep(1)
			exit()