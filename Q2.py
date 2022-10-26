password_ls = ['ABd1234@1','F1#','2w3E*','2We3345','2eWrtgs#dv']
cond1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cond2 = ['0','1','2','3','4','5','6','7','8','9']
cond3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cond4 = ['$','#','@']

valid_pw_ls = []

def password_check(password_ls):
    for pw in password_ls:
        small = 0
        nums = 0
        caps = 0
        special_char = 0
        if len(pw)>=6 and len(pw)<=12:
            for i in pw:
                if i in cond1: 
                    small += 1
                if i in cond2: 
                    nums +=1
                if i in cond3:
                    caps += 1
                if i in cond4: 
                    special_char += 1
        if small>=1 and nums>=1 and caps>=1 and special_char>=1: 
            valid_pw_ls.append(pw)
            print(pw)
    return valid_pw_ls

obj = password_check(password_ls)
print("Valis Password is :{}".format(obj))


