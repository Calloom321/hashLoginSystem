from register import *
from access import *
import hashlib
import os

def beginning():
    accountStatus = input("Are you an exisiting user? ").title()
    if accountStatus == "Yes" or accountStatus == "Y":
        login()
    elif accountStatus == "No" or accountStatus == "N":
        createAccount()

    else:
        print("Please type 'Yes' or 'No'")
        return beginning()


beginning()
