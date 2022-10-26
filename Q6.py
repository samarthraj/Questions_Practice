
def compute_add(a):

    val1 = str(a)
    val2 = (str(a) + str (a)) 
    val3 = (str(a) + str (a) + str (a)) 
    val4 = (str(a) + str (a) + str (a) + str (a))  

    result = int(val1) + int(val2) + int(val3) + int(val4)
    return result 

a = int(input('Type in a number:')) #converting str to int simply, input function always is str intake
output = compute_add(a)
print(output)

