

output = ''
def pass_list(ls):
    for i in range(0,len(ls)-1):
        if (ls[i] == ls[i+1]):
            #print(ls[i])
            #print(ls[i+1])
            output = 'True'
        else:
            output = 'False'

    return output
ls = ['a','a','a','a','d']
output = pass_list(ls)
print(output)