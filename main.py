from cryptography.fernet import Fernet

master_pw = "Master"
# Use this function just once to generate the key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        file = open("key.key", "rb")
        key = file.read()
        file.close()
        return key

# write_key()

def load_key():
    return open("key.key", "rb").read()
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ",  fer.decrypt(passw.encode()).decode())

key = load_key()
fer = Fernet(key)

def add():
    name = input("Account Name: ")
    pwd = input("Password : ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    userPassword = input("Type in the master password ")
    if master_pw == userPassword:
        mode = input("Add new password or view existing ones? (view, add), press q to quit \n").lower()
        if mode == "q":
            break
        if mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("invalid mode.")
            continue
    else:
        print("Master password wasn't right")