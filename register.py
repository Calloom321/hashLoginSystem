from access import *
import hashlib
import os



def hash_password(password):
    return hashlib.sha3_512(str.encode(password)).hexdigest()

def checkHash(password, hash):
    return hash_password(password) == hash


def continueCheck():
 
    checkContinue = input("Would you like to login? Yes or No ").title()
    if checkContinue == "Yes" or checkContinue == "Y":
        login()
    elif checkContinue == "No" or checkContinue == "N":
        print("Okay, have a great day!")
    else:
        print("Unknown error")
        return continueCheck()

def createAccount():
  
    accounts = open("accounts.txt", "r")
    username = input ("Please create your username: ")

    password = input ("Please create your password: ")
    password = hash_password(password)
    correctPassword = input ("Please retype your password: ")
    correctPassword = hash_password(correctPassword)

    userList = []
    passwordList = [] 

    for i in accounts:
        a,b = i.split(", ")
        b = b.strip()
        userList.append(a)
        passwordList.append(b)

    data = dict(zip(userList, passwordList))


    if password != correctPassword:
        print("Your passwords don't match, please try again")
        return createAccount()
    
    else:
        if len(password) <= 6:
            print("Your password is too short, please try again")
            return createAccount()
        
        elif username in userList:
            print("Username is already taken, please try again")
            return createAccount()
        
        else:
            accounts = open ("accounts.txt", "a")
            accounts.write(username + ", " + password + "\n")
            print("Account Created")
            accounts.close()
            continueCheck()
          

                
      


