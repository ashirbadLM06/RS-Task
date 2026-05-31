users={
    'admin':'pass1123',
    'surya':'s@2007',
    'king':'g@#59*'
}

attempts=3
while attempts>0:
    username=input("Enter Username: ")
    password=input("Enter Password: ")
    if username in users and users[username]==password:
        print("Login Successful.")
        break
    else:
        attempts-=1
        print(f"Invalid Usename or Password.")

        print(f"Attempts Left: {attempts}")
    if attempts == 0:
       print("Account Locked.")