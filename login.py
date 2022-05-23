import random
import atm
import psycopg2


username = input('Please enter your username >>> \n')
password = input('Please enter your password >>> \n')
login_code = random.randint(1000,5000)


connection = psycopg2.connect('dbname=test1')
connect = connection.cursor()
username_query = connect.execute(f"SELECT username FROM account WHERE username = '{username}';") # I used double quotes here to escape the single quotes required for the SQL username Query
user_result = connect.fetchall()
user = user_result[0]
account_user = user[0]
password_query = connect.execute(f"SELECT password FROM account WHERE username = '{username}';")
password_result = connect.fetchall()
accept_password = password_result[0]
account_password = accept_password[0]







if username == account_user and password == account_password:
        print('Here is your login code :: \n', login_code)

while True:
    if username == account_user and password == account_password:
        login_verify = int(input('Enter the login code sent to your device >>>'))
        if login_code == login_verify:
            print('Welcome')
            atm.exe()
            break
        else:
            print('Incorrect code')
            continue
    elif username in account_user and password != account_password:
        print('wrong password, try again')
    elif username not in account_user and password == account_password:
        print(f'sorry,{username} is not registered. Try again')
        continue
    elif username not in account_user and password != account_password:
        print('your username and password are incorrect, check correctly and try again')