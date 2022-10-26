
ls = []
special_char_ls = ['!','@','#','$','%','^','&','*',' ']

def upper_lower_case_count(sentence):
    count_upper = 0
    count_lower = 0
    for i in sentence:
        ls.append(i)
    
    for j in ls:
        if j == j.upper() and (j not in special_char_ls):
            count_upper += 1
        elif j == j.lower() and (j not in special_char_ls):
            count_lower += 1
    
    return (count_upper,count_lower)
        
sentence = 'Hello World'
output = upper_lower_case_count(sentence)
print(output)
