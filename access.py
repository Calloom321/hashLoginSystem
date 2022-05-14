from turtle import rt
from register import *
import webbrowser
import hashlib
import os


def hash_password(password):
    return hashlib.sha3_512(str.encode(password)).hexdigest()

    
clear = lambda: os.system('cls')

def login():

    accounts = open("accounts.txt", "r")
    username = input ("Enter your username: ")
    password = input ("Enter your password: ")
    password = hash_password(password)

    if not len(username or password) <= 1:

        userList = []
        passwordList = []

        for i in accounts:
            a,b = i.split(", ")
            b = b.strip()
            userList.append(a)
            passwordList.append(b)
        
        data = dict(zip(userList, passwordList))

        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("Login Successful")
                        print(f'Welcome {username}')
                        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                    
                    else:
                        print("username or password invalid, please try again")
                        accounts.close()
                        return login()
                except:
                    print("username or password invalid, please try again")
                    accounts.close()
                    return login()
            else:
                print("user doesn't exist, please try again")
                accounts.close()
                return login()

        except:
            accounts.close()
            print("unknown user, please try again")
            return login()
    else:
        print("Please enter a value")
        return login()