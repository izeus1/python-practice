#문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요
import sys

value = int(input('수를 입력하세요: '))

#while value.isdigit() is True:
#    print("정수를 입력 하세요")
#    break

#while True:
#    if (str(value).isdigit()) is True:
#        print("정수를 입력 하세요")
#    elif value % 3 == 0:
#        print("3의 배수입니다.")
#    else:
#        print("3의 배수가 아닙니다.")

try:
    if value == 0:
        print("0입니다.")
    elif value % 3 == 0:
        print("3의 배수입니다.")
    else:
        print("3의 배수가 아닙니다.")
except:
    print("정수를 입력하세요.")

