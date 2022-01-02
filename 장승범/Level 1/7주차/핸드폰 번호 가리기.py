def solution(phone_number):
    
    result = phone_number[::-1][:4]
    
    for i in range(len(phone_number[::-1][4:])):
        result += '*'
      
    return result[::-1]