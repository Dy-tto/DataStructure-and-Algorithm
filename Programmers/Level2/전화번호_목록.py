def solution(phone_book):
    answer=True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
                answer = False
                break
    return answer

# import re
# def solution(phone_book):
#     answer = True
#     phone_book.sort(key=lambda x:int(x))
#
#     for i in range(len(phone_book)-1):
#         regex=re.compile(f'^{phone_book[i]}')
#
#         for j in range(i+1,len(phone_book)):
#             m=regex.match(phone_book[j])
#             if m:
#                 answer=False
#                 break
#         if answer==False:
#             break
#     return answer
