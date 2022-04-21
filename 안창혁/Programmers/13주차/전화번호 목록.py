def solution(phone_book):
    
    phoneBook = sorted(phone_book)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

## 시간초과
#     for i in range(len(phone_book)):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i].startswith(phone_book[j]):
#                 return False
#             elif phone_book[j].startswith(phone_book[i]):
#                 return False
    
#     return True