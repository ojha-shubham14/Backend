username = input("enter your user name : ")
password = input("enter your password : ")
password_len = len(password)
hidden_password = password_len*'*'
print(f"{username} password is {hidden_password} and it is {password_len} letter long")

