# I ONLY USED THIS CODE TU GENERATE THE HASH OF EACH FILE

import hashlib
import argparse
import os


parser = argparse.ArgumentParser(description="Description")
parser.add_argument("-file", type=str, help="asdf")
data = parser.parse_args()

try:
	# We try to open the file you added
	file = open(data.file, "rb")
	# We save the content in 'info'
	info = file.read()

	# Finaly, we generate the hash
	the_hash = hashlib.sha512(info)
	hashed = the_hash.hexdigest()
	print(hashed)
except:
	print("[!] 'Hash.py' has to be in the same folder than")
	print("::: the file")