import time
import re
import os

try:
	from pyhunter import PyHunter

except:
	print("[!] Installing necesary modules...")
	os.system("pip install PyHunter")
	print()

	print("::: Cleaning terminal")
	os.system("cls")

	print("::: Executing the program again...")
	print()
	os.system("App.py")
	exit()


class Hunter:

	def __init__(self, apikey, domain):

		self.limit = 1

		self.setAPIKey(apikey)
		self.apikey = self.getAPIKey()

		self.setDomain(domain)
		self.domain = self.getDomain()


	def setAPIKey(self, apikey):
		if len(apikey) == 40:
			print("[*] Valid API key")
			self.apikey = apikey

		else:
			print("[!] This is not a Hunter api key")
			print("::: Closing program")
			time.sleep(1)

	def getAPIKey(self):
		return self.apikey


	#########################################################################
	def setDomain(self, domain):
		set_domain = re.match(r'(www.\w*.com|\w*.com|\w*)', domain)

		if(set_domain):
			print("[*] Valid domain")
			self.domain = domain

		else:
			print("[!] This is not look like a domain,")
			print("::: add the information again.")

			print("::: The domain should have one of the next aspects:")
			print("::::: www.domain.com")
			print("::::: domain.com")
			print("::::: domain")

			print("::: Closing program...")
			time.sleep(1)
			exit()

	def getDomain(self):
		return self.domain


	#########################################################################
	def search(self):
		hunter = PyHunter(self.apikey)
		result = hunter.domain_search(company=self.domain, limit=self.limit, emails_type='personal')

		return result


	def showInfo(self, results):
		try:
			if results['domain'] == None:
				print("[!] We do not find the organization")

			else:
				print('Domain: ' + results['domain'])
			
				if results['organization'] == None:
					print("[!] Organization no found")
				
				else:
					print('Organization name: ' + results['organization'])
					
					if results['emails'] == None:
						print('[!] No emails or names found')
					
					else:
						print('Personal emails found: ' + results['emails'][0]['value'])
						print('Personal names found: ' +
							   results['emails'][0]['first_name'] +
							   ' ' + results['emails'][0]['last_name'])

		except:
			print("[!] Error")
			print("::: Closing program...")
			time.sleep(1)


	def saveInfo(self, results):
		try:
			file = open('Hunter' + self.domain + '.txt', 'w')
			if results['domain'] is None:
				pass
			else:
				file.write('Domain: ' + results['domain'] + '\n')
			if results['organization'] is None:
				pass
			else:
				file.write('Organization name: ' + results['organization'] + '\n')
			if len(results['emails']) == 0:
				file.write('No emails or names found')
			else:
				file.write('Personal emails found: ' + results['emails'][0]['value'] + '\n')
				file.write('Personal names found: ' + results['emails'][0]['first_name'])
				file.write(' ' + results['emails'][0]['last_name'] + '\n')
			file.close()

		except:
			print("[!] Error")
			print("::: Closing program...")
			time.sleep(1)