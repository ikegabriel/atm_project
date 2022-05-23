import psycopg2

connection = psycopg2.connect('dbname=test1')
connect = connection.cursor()
balance_request = connect.execute('SELECT account_balance FROM account;')
result = connect.fetchall()
real_account = result[0]
account_balance = real_account[0]


userpin = 1451

def electricity():

    distributor = input('''Choose your electricity distributor \n
            1 for EEDC
            2 for EKEDC
            3 for KEDC
            4 for AEDC
    \n >>>:''')

    meter = int(input('Enter your meter number >>>:'))
    amount = int(input('Enter the amount you wish to purchase >>>:'))
    pin = int(input('Enter your pin >>>:'))
    if pin == userpin:
        debit = account_balance - amount
        connect.execute(f'UPDATE account SET account_balance = {debit} WHERE id = 1;')
        connection.commit()
        print(f'Purchase succesful')
        print(f'You purchased electricity of {amount}, your balance is {debit}')

def internet():
    distributor = input('''Choose your internet provider \n
                1 for Swift
                2 for Tizeti
                3 for Mtn
                4 for Vodafone
        \n >>>:''')

    router = int(input('Enter your router number >>>:'))
    amount = int(input('Enter the amount you wish to purchase >>>:'))
    pin = int(input('Enter your pin >>>:'))
    if pin == userpin:
        debit = account_balance - amount
        connect.execute(f'UPDATE account SET account_balance = {debit} WHERE id = 1;')
        connection.commit()
        print(f'Purchase succesful')
        print(f'You purchased internet of {amount}, your balance is {debit}')


def phone():
    provider = input('''Choose your network provider \n
                1 for Airtel
                2 for Glo
                3 for Mtn
                4 for 9mobile
        \n >>>:''')

    phone_number = int(input('Enter your phone number >>>:'))
    amount = int(input('Enter the amount you wish to purchase >>>:'))
    pin = int(input('Enter your pin >>>:'))
    if pin == userpin:
        debit = account_balance - amount
        connect.execute(f'UPDATE account SET account_balance = {debit} WHERE id = 1;')
        connection.commit()
        print(f'Recharge succesful')
        print(f'You purchased airtime of {amount}, your balance is {debit}')
