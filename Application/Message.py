import time

class Message:

	def __init__(self):
		self.message = ""
		self.language = 0
		self.words_list = []

	################################################################
	def spanishDictionary(self):
		# Abrimos nuestro Archivo txt para leer
		file = open("dictEsp.txt", "r", encoding="utf-8")

		# Creamos una lista donde guardaremos las pa-
		# labras de nuestro txt
		# * NO QUISE USAR UN DICCIONARIO (set()) POR-
		#   QUE DESPUES PIERDE EL ORDEN ALFABETICO
		dictionary = []

		for word in file:
			# Nos aseguramos de que las palabras no
			# incluyan un salto de linea ('\n') o 
			# un espacio (' ')
			word = word.replace("\n", "")
			word = word.replace(" ", "")
			word = word.lower()
			dictionary.append(word)
		# Como el contenido del txt ya esta en nuestro
		# dictionary ya podemos cerrarlo
		file.close()

		# Como el mensaje cifrado va a contener espacios
		# agregamos uno a la lista
		dictionary.append(" ")

		numbers = "0123456789"
		for number in numbers:
			dictionary.append(number)

		return dictionary


	def englishDictionary(self):
		# We open aour txt file
		file = open("dictEng.txt", "r", encoding="utf-8")

		# We create a list to save there our dictionary
		# words
		# I DID NOT WANT TO USE A TRUE DICTIONARY (set())
		# BECAUSE IT CHANGE THE ORDER OF WORDS
		dictionary = []

		for word in file:
			# We delete \n and spaces of our word
			word = word.replace("\n", "")
			word = word.replace(" ", "")
			word = word.lower()
			dictionary.append(word)
		file.close()

		# The encodable message can have spaces, we
		# add one in the list
		dictionary.append(" ")

		# We the numbers to the dictionary too
		numbers = "0123456789"
		for number in numbers:
			dictionary.append(number)


		return dictionary


	######################################################################
	def setLanguage(self, language):
		if language == 1:
			language = 0
			self.language = True

		elif language == 2:
			language = 0
			self.language =  False

		else:
			print()
			print("[!] This option does not exist")
			print("::: Closing program...")
			time.sleep()
			exit()

	def getLanguage(self):
		return self.language


	#######################################################################
	def setMessage(self, message):
		if len(message) >= 3:
			print("[*] Valid Message")
			self.message = message.lower()

		else:
			print(":[!] You have to add longer message")
			exit()
			print()


	def getMessage(self):
		return self.message


	######################################################################
	def messageWords(self, sentence):
		cont = 0
		word = ""
		message = sentence + " "
		words_list = []

		# We read each letter of message
		for words_msg in message:

			# The sentences has to have an space, so, we 
			# add this one to the list
			if words_msg == " ":
				words_list.append(word)
				word = ""

			else:
				# If 'words_msg' is different to " ", we
				# the letter in 'word'
				word = word + words_msg

		cont = 0
		nwords_list = []

		# We do not want spaces in the list, so we search
		# for each word
		for find_space in words_list:
			# If we saved a word with a space, we delete it
			without_space = find_space.replace(" ", "")

			# We save the word without spaces in a new list
			if without_space != "":
				nwords_list.append(without_space)
			cont = cont + 1

		self.words_list = nwords_list

		# We do not need more the new list, so, we
		# delete it
		del nwords_list

		return self.words_list

	######################################################################
	def verifyLanguage(self, sentence):
		# We call messageWords() to know what is the
		# language our user chose
		words_list = self.messageWords(sentence)
		word_found = 0

		# If we enter in one of the next conditionals,
		# we would be verifying if the message was
		# wrote in that language
		if self.getLanguage() == True:
			for word_list in words_list:
				for dict_word in self.englishDictionary():
					if word_list == dict_word:
						word_found = word_found + 1

		elif self.getLanguage() == False:
			for word_list in words_list:
				for dict_word in self.spanishDictionary():
					if word_list == dict_word:
						word_found = word_found + 1

		if word_found > 0:
			average = (word_found * 100) / len(words_list) 
			return average
		else:
			return 0