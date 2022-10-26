
def bank_transaction(DW_ls,amount_ls):
    deposit_amt = 0
    withdraw_amt = 0 
    for i in range(0,len(DW_ls)):
        for j in range(0,len(amount_ls)):
            if DW_ls[i] == 'D':
                if i == j: #if index are same 
                    deposit_amt += amount_ls[j]
            elif DW_ls[i] == 'W':
                if i == j:
                    withdraw_amt += amount_ls[j]
    
    balance = deposit_amt - withdraw_amt
    return balance

DW_ls = ['D','D','W','D']
amount_ls = [300,300,200,100]

output = bank_transaction(DW_ls,amount_ls)
print('Tha Balance amount is {}'.format(output))