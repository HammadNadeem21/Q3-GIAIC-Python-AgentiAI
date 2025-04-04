from hashlib import sha256

def hash_pass(password):

    return sha256(password.encode()).hexdigest()



def login(email, stored_logins, password_to_check):

    if stored_logins[email] == hash_pass(password_to_check):
        return True
    
    return False

def main():

    stored_logins = {
        "example@gmail.com": "50d858e0985ecc7f60418aaf0cc5ab587f42c2570a884095a9e8ccacd0f6545c",
        "hammad@gmail.com": "4ec0fd7916e201d92f7ba220d13f227794d2c37fd91b8d5c733c0491e71d53a6",
        "hamid@gmail.com": "b36ffc3cea02a265926cab0e3bb647aace65345d7999c8604b2a3067fdc6f234"
    }

    print(login("example@gmail.com", stored_logins, "example"))  
    print(login("example@gmail.com", stored_logins, "pass"))

    print(login("hammad@gmail.com", stored_logins, "hammad"))  
    print(login("hammad@gmail.com", stored_logins, "command"))

    print(login("hamid@gmail.com", stored_logins, "hamid"))  
    print(login("hamid@gmail.com", stored_logins, "hammad"))  



if __name__ == '__main__':
    main()