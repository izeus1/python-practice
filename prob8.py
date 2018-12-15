#문제 8.
#키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

a = []
value1 = int(input('1번 수를 입력하세요: '))
a.append(value1)
value2 = int(input('2번 수를 입력하세요: '))
a.append(value2)
value3 = int(input('3번 수를 입력하세요: '))
a.append(value3)
value4 = int(input('4번 수를 입력하세요: '))
a.append(value4)
value5 = int(input('5번 수를 입력하세요: '))
a.append(value5)

print(a)
avg = sum(a, 0)/len(a)
print(int(avg))
