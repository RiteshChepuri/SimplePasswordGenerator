import random
import string
from random_word import RandomWords 
import pyperclip as pc

master_pswd  = "123456" 


print("Welcome To Password Generator")

pswd = input("Enter Your Master Password\n")

while pswd != master_pswd:
    pswd = input("Wrong Password Try Again\nTo Quit enter Q\n")
    if pswd == "q" or pswd == "Q":
        break

if pswd == master_pswd:
    print("New Password Generating Process")
    service = input("What is the name of the Service?\n")
    r = RandomWords()
    word = r.get_random_word(hasDictionaryDef="true",includePartOfSpeech="noun",minLength=5, maxLength=6)
    temp_length = input("Enter the length of the required password\n")
    temp_length_ = int(temp_length)
    length = temp_length_ - 4
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    symbols = string.punctuation
    all = lower+upper+number+symbols
    rand_pick = random.sample(all,length)
    temp_password = "".join(rand_pick)
    password = temp_password + word
    pc.copy(password)
    print(password,end=" ")
    print("is Your Password for the ", end="" )
    print(service)