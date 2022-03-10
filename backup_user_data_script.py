#windows 7 backup data script testing

import os
from webbrowser import selenium


#os.mkdir('C:\Users\inapoli\Desktop\test')
def get_userName():
    print("Please enter the user name to be transferred:\n")
    userName = input()
    print("Hello ", userName)
    return userName

print("Hello")
get_userName()

