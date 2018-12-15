#문제6.
#주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

value = int(input('수를 입력하세요: '))

#range에 들어갈 값
valueone = value + 1
count=0
sum=0
for n in range(1, valueone):
    if n%3 == 0:
        count += 1
        sum += n

print("주어진 리스트에서 3의 배수의 개수", count, "\n","주어진 리스트에서 3의 배수의 합", sum)




