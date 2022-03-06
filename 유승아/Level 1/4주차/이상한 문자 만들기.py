def solution(s):
    string_list = s.split(" ")
    
    for i in range(len(string_list)):
        s_list = list(string_list[i]) 
        for j in range(len(s_list)): 
            if j % 2 == 0: 
                s_list[j] = s_list[j].upper() 
            else: 
                s_list[j] = s_list[j].lower() 
        string_list[i] = "".join(s_list)

        
    return " ".join(string_list)