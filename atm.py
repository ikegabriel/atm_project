

pin = 1451
account_balance = 5000000

operations = '''
                Press 1 for cash withdrawal
                Press 2 for cash transfer
                Press 3 for pay bills
                Press 4 to check your account balance
'''


def cash_withdrawal():
    amount = int(input('Enter amount >>>:'))
    pin_input = int(input('Enter your pin >>>:'))
    if pin_input == pin:
        debit = account_balance - amount
        new_balance = debit
        print('Please take your cash')
        print(f'Debit of {amount} Naira, your balance is {new_balance} Naira')

def transfer():
    amount = int(input('Enter amount >>>:'))
    recipient_account = int(input('Enter recipient account number >>>:'))
    recipient_bank = input('Enter recipient bank')
    pin_input = int(input('Enter your pin >>>:'))
    if pin_input == pin:
        transfer = account_balance - amount
        new_balance = transfer
        print('Transfer Succesful')
        print(f'You made a transfer of {amount} Naira, your balance is {new_balance} Naira')

def check_balance():
    pin_input = int(input('Enter your pin >>>:'))
    if pin_input == pin:
        print(f'Your account balance is {account_balance}')


def pay_bills():
    bill_operation = print('''
                        Press 1 to pay electricity bill
                        Press 2 to pay water bill
                        Press 3 to pay internet bill
                        press 4 to pay phone bill
    ''')
    bill_select = int(input('Select bill >>>:'))

    try:
        if bill_select == 1:
            electricity()
        elif bill_select == 2:
            water()
        elif bill_select == 3:
            internet()
        elif bill_select == 4:
            phone()
    except:
        print('Wrong Input')




def exe():
    print(operations)
    operation = int(input('Select Operation >>>:'))
    if operation == 1:
        cash_withdrawal()
    elif operation == 2:
        transfer()
    elif operation == 4:
        check_balance()


#cash_withdrawal()