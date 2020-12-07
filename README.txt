::::::::::::::::::::::::::::::::::::::::::::::::::::P R O Y E C T O::::::::::::::::::::::::::::::::::::::::::::::::::::
=======================================================================================================================
The aplication code has the next options for you:
1. Encode a Message
2. Unencode a Message
3. Hack an encoded Message
4. Investigate an organization (with your hunter api key)
5. Send Messages for Gmail.com or Outlook.com
_______________________________________________________________________________________________________________________
Now we will explain which parameters you have to add for each option:
---If you need help for the parameters you can execute 'Application.py -h'---
-----------------------------------------------------------------------------------------------------------------------
[*] If you want to ENCODE a message, these are the possible options:
	-opc 1
		-lang *Choose a language with 1 or 2*
			-msg *"Write your encodable message"*
				-t_cifr 1 -rot *Add a number between 1-25*
				-t_cifr 2 -key *"Write your key"*

[+] Example(s):
:::: Application.py -opc 1 -lang 1 -msg "This is my message in english" -t_cifr 1 -rot 13
:::: Application.py -opc 1 -lang 2 -msg "Este es mi mensaje en español" -t_cifr 2 -key "keyword"
-----------------------------------------------------------------------------------------------------------------------
[*] If you want to UNENCODE a message, these are the possible options:
	-opc 2
		-lang *Choose a language with 1 or 2*
			-msg *"Write your encodable message"*
				-t_cifr 1 -rot *Add a number between 1-25*
				-t_cifr 2 -key *"Write your key"*

[+] Example(s):
:::: Application.py -opc 2 -lang 1 -msg "guvf vf zl zrffntr va ratyvfu" -t_cifr 1 -rot 13
:::: Application.py -opc 2 -lang 2 -msg "e s lsmaetijse ep m aeeeñsnno" -t_cifr 2 -key "keyword"
-----------------------------------------------------------------------------------------------------------------------
[*] If you want to HACK an encoded message, these are the possible options:
	-opc 3
		-lang *Choose a language with 1 or 2*
			-msg *"Write your encodable message"*
				-t_cifr *Choose a type of hacking writing the number 1 or 2*

[+] Example(s):
:::: Application.py -opc 3 -lang 1 -msg "guvf vf zl zrffntr va ratyvfu" -t_cifr 1
:::: Application.py -opc 3 -lang 2 -msg "e s lsmaetijse ep m aeeeñsnno" -t_cifr 2
-----------------------------------------------------------------------------------------------------------------------
[*] If you want to GET INFORMATION of an ORGANIZATION with your HUNTER api key,
::: these are the possible options:
	-opc 4
		-apikey *"Write your api key"*
			-domain *"Write the domain"*

[+] Example(s):
:::: Application.py -opc 4 -apikey '31mn93abbx811o05q119lDp1mms931ml5c31jjj7' -domain "www.telmex.com"
:::: Application.py -opc 4 -apikey '31mn93abbx811o05q119lDp1mms931ml5c31jjj7' -domain "telmex.com"
:::: Application.py -opc 4 -apikey '31mn93abbx811o05q119lDp1mms931ml5c31jjj7' -domain "telmex"
-----------------------------------------------------------------------------------------------------------------------
[*] If you want to SEND an EMAIL (you can also ADD a PICTURE in your email):
	-opc 5
		-t_email *Choose the type of email with 1 or 2*
			-email *"Write your email"*
				-passw *"Write your email password"*
					-to  *"Write the email of your friend"*
						-subj *"Write the subject of your message"*
							-msg *"Write your message"*
								# (OPTIONAL) #
								-pic *"Write the name of your image","Write the directory of your image"*

[+] Example(s):
:::: Application.py -opc 5 -t_email 1 -email "example@gmail.com" -passw "yourpassword" -to "example2@account.com" 
-subj "Subject:" -msg "Your message" -pic "Picture.jpg","C:\Users\UserName\Documents"

:::: Application.py -opc 5 -t_email 2 -email "example@outlook.com" -passw "yourpassword" -to "example2@account.com" 
-subj "Subject:" -msg "Your message" -pic "Picture.jpeg","C:\Users\UserName\Documents"

:::: Application.py -opc 5 -t_email 1 -email "example@gmail.com" -passw "yourpassword" -to "example2@account.com" 
-subj "Subject:" -msg "Your message" -pic "Picture.jpg","C:\Users\UserName\Documents"

:::: Application.py -opc 5 -t_email 2 -email "example@outlook.com" -passw "yourpassword" -to "example2@account.com" 
-subj "Subject:" -msg "Your message"
-----------------------------------------------------------------------------------------------------------------------
[*] If you want to verify if a PORT is OPEN:
	-opc 6
		-ip *"Write the IP"*
			-port *Write the port you want to verify*

[+] Example(s):
:::: Application.py -opc 6 -ip "192.168.1.12" -port 8080
-----------------------------------------------------------------------------------------------------------------------
[*] If you want to verify the DNS:
	-opc 7

[+] Example(s):
:::: Application.py -opc 7
-----------------------------------------------------------------------------------------------------------------------