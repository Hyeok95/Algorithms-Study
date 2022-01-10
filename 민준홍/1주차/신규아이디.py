import re
#정규표현식 기본 표현들 ( {n,m} , [a-zA-Z], [ㄱ-ㅎㅏ-ㅣ] , ()(),  ^abc ) 
#메타 문자 . ^ $ * + ? \ | ( ) { } [ ]

def solution(new_id):
    new_id = new_id.lower()
    new_id_revised = ''
    for i in new_id:
        if i == "." or i == "_" or i == "-" or i.isalpha() == True or i.isdigit() == True:
            new_id_revised += i
    new_id_revised = re.sub('\.+', '.', new_id_revised)
    new_id_revised = re.sub('^[.]|[.]$', '', new_id_revised)
    if len(new_id_revised) == 0:
        new_id_revised = "a"
    if 16 <= len(new_id_revised):
        new_id_revised = new_id_revised[:15]
        if new_id_revised[-1] == ".":
            new_id_revised =  new_id_revised[:-1]
    if len(new_id_revised) <= 2:
        while len(new_id_revised) < 3:
            new_id_revised += new_id_revised[-1]
        
        
    
    
    return new_id_revised