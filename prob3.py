#문제3. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

#1번
import os

s='/usr/local/bin/python'
s_array = s.split('/')
for i in s_array[1:]:
    print("'{0}'".format(i), end = '')

# for s in s_array:
#     print("'" + s + "'" + ",", end='')

#
# print("")

#2번
# s = '/usr/local/bin/python'
# a = os.path.split(s)
# print(a)

# print("")
#2번 다른 방향
# s = '/usr/local/bin/python'
# a = s.split('/')
# for aa in range(1, 4):
#     print("/"+ aa, end='')
#
# for bb in range(4,4):
#     print("/"+ bb, end='')

max = len(s_array)
for i in range(1, max-1):
    print("/" + "{0}".format(i), end='')




