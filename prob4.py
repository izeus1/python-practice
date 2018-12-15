#문제4. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.
#(정규표현식 사용)

# s = """
# <html>
#     <body style='background-color:#ffff'>
#         <h4>Click</h4>
#         <a href='http://www.python.org'>Here</a>
#         <p>
#         	To connect to the most powerful tools in the world.
#         </p>
#     </body>
# </html>"""

#답 코드 - <> 태크로 감싼 정보 제거!,
 # while True:
 #     first = s.find("<") # <를 가진 번호 저장.
 #     last = s.find(">")+1# >를 가진 번호 저장장
# #만일, < 있다면 >까지 삭제
#     if first != -1: #find로 검색하여, "<" 있다면
#         for i in
#             del s[:last]
from os import remove

s = "<html>text<body> "
# first = s.find("<") #0번
# last = s.find(">")+1 #6
#
# s_list = list(s)
# print(s_list)    #리스트로 저장
# # del s_list[0]
#
# while True:
#     first = s.find("<") # <를 가진 번호 저장.
#     last = s.find(">")+1# >를 가진 번호 저장장
#
#     if first != -1:
#         for i in s_list: #
#             del s_list[i]
#         else:
#             break
#
# print(s_list)

s_list = list(s)
result = []
for i in s_list[0:]:
    print(i, end='')

if first =
del s_list[0:5]
print(s_list)












