import Message
import math

class Transposition(Message.Message):

	def __init__(self):
		super().__init__()
		self.key = 0

	def setKey(self, key):
		if len(key) >= len(self.message):
			key = ""
			print(":[!] You added a key longer / equal than message")
			exit()

		if " " in key:
			key = ""
			print(":[!] You added a space in the key")
			exit()

		elif key.isalpha() == False:
			key = ""
			print(":[!] The key only allows letters")
			exit()

		else:
			self.key = len(key)

	def getKey(self):
		return self.key


	######################################################################
	def encodeMessage(self):
		if super().verifyLanguage(super().getMessage()) < 50:
			print(":[!] For encoding mode, we only accept english / spanish sentences")
			exit()
		else:
			message = super().getMessage()
			key = self.getKey()
			columns = [''] * key
			counter = 0

			for letter in message:
			    while counter < key:
			        columns[counter] = columns[counter] + letter
			        counter = counter + 1
			        break

			    if counter == key:
			        counter = 0

			encoded_message = ""
			for column in columns:
				encoded_message = encoded_message +  column

			return encoded_message

	# The transposition decrypt function will simulate the "columns" and
	# "rows" of the grid that the plaintext is written on by using a list
	# of strings. First, we need to calculate a few values.
	def unencodeMessage(self):
		message = super().getMessage()
		key = self.getKey()

		# The number of "columns" in our transposition grid:
		n_columns = int(math.ceil(len(message) / float(key)))
		# The number of "rows" in our grid will need:
		n_rows = key
		# The number of "shaded boxes" in the last "column" of the grid:
		n_shaded_boxes = (n_columns * n_rows) - len(message)

		# Each string in plaintext represents a column in the grid.
		plaintext = [''] * n_columns

		# The column and row variables point to where in the grid the next
		# character in the encrypted message will go.
		column = 0
		row = 0

		for letter in message:
			plaintext[column] += letter
			column += 1 # Point to next column.

			# If there are no more columns OR we're at a shaded box, go back to
			# the first column and the next row:
			if (column == n_columns) or (column == n_columns - 1 and row >= n_rows - n_shaded_boxes):
				column = 0
				row += 1

		unencodeMessage = ''.join(plaintext)
		if super().verifyLanguage(unencodeMessage) >= 50:
			return unencodeMessage

		elif super().verifyLanguage(unencodeMessage) < 50:
			print(":[!] We are sorry, we can not decode the message.")
			print(":::: We only accept english / spanish, maybe")
			print(":::: you the original message is wrote in a ")
			print(":::: different language, or you added an incorrect")
			print(":::: key.")
			return ""


	def hackMessage(self):
		if super().verifyLanguage(super().getMessage()) > 60:
			print(":[!] This message is not encoded")
			print(super().verifyLanguage(super().getMessage()))
			exit()
		else:
			message = super().getMessage()

			for key in range(1, len(message)):

				# The number of "columns" in our transposition grid:
				n_columns = int(math.ceil(len(message) / float(key)))
				# The number of "rows" in our grid will need:
				n_rows = key
				# The number of "shaded boxes" in the last "column" of the grid:
				n_shaded_boxes = (n_columns * n_rows) - len(message)

				# Each string in plaintext represents a column in the grid.
				plaintext = [''] * n_columns

				# The column and row variables point to where in the grid the next
				# character in the encrypted message will go.
				column = 0
				row = 0

				for letter in message:
					plaintext[column] += letter
					column += 1 # Point to next column.

					# If there are no more columns OR we're at a shaded box, go back to
					# the first column and the next row:
					if (column == n_columns) or (column == n_columns - 1 and row >= n_rows - n_shaded_boxes):
						column = 0
						row += 1

				unencodeMessage = ''.join(plaintext)
				if super().verifyLanguage(unencodeMessage) > 60:
					return unencodeMessage
					break

			if super().verifyLanguage(unencodeMessage) <= 60:
				print(":[!] We are sorry, we can not hack the message")
				print(":::: we only accept english / spanish, maybe")
				print(":::: you the original message is wrote in a ")
				print(":::: different language")
				exit() 