import random
import atm

allowed_users = 'abeldeen2', 'sambuo', 'jiji204'
allowed_password = '12345'

username = input('Please enter your username >>> \n')
password = input('Please enter your password >>> \n')
login_code = random.randint(1000,5000)

if username in allowed_users and password == allowed_password:
        print('Here is your login code :: \n', login_code)

while True:
    if username in allowed_users and password == allowed_password:
        login_verify = int(input('Enter the login code sent to your device >>>'))
        if login_code == login_verify:
            print('Welcome')
            atm.exe()
            break
        else:
            print('Incorrect code')
            continue
    elif username in allowed_users and password != allowed_password:
        print('wrong password, try again')
    elif username not in allowed_users and password == allowed_password:
        print(f'sorry,{username} is not registered. Try again')
        continue
    elif username not in allowed_users and password != allowed_password:
        print('your username and password are incorrect, check correctly and try again')