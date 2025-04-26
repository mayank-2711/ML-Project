from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)

def load_key():
    file = open("key.key",'rb')
    key = file.read()
    file.close()
    return key
cnt = 1
while True:
    master_pwd = input('What is the master password? ')
    if (master_pwd != 'PwdMngr') and (cnt < 3):
        print("::Password Incorrect, please try again::")
        cnt += 1
    elif (master_pwd != 'PwdMngr') and (cnt >= 3):
        print('::Password Incorrect, Attempt Limit exceeded::')
        exit()
    else:
        break

key = load_key()
fer = Fernet(key)



def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            user, passw = line.rstrip().split("|")
            print("User:",user, "Password:", (fer.decrypt(passw.encode())).decode())


def add():
    name = input('Account name: ')
    pwd = input("Password: ")

    with open('password.txt','a') as f:
        f.write(name + "|" + (fer.encrypt(pwd.encode()).decode()) + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones?")
    if mode == "q":
        print("Thank you")
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
