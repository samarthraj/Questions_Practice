
correct_ls = []
reverse_ls = []
output_text = ''
def palindrome(word):
    for i in word:
        correct_ls.append(i)
    
    for j in range(1,len(correct_ls)+1):
        print(correct_ls[-j])
        reverse_ls.append(correct_ls[-j])
    
    if correct_ls == reverse_ls: 
        output_text = 'Its a Palindrome'
    else:
        output_text = 'Not a Palindrome'
    
    return output_text

word = 'ARAD'
output = palindrome(word)
print(output)