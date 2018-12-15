#문제9.
#문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

value = input('문자열을 입력하세요: ') #input의 기본 리턴 타입: str

a = []
a = list(value)

b= a[::-1]

for bb in b:
    print(bb, end='')


#def reverse(s):
