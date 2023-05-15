# generate a password
import random
import string
import os

a = string.ascii_uppercase + string.ascii_lowercase + string.punctuation


def generate_password(value, quantity = 1):
    '''this function get the number of characters (value) and generate a random password'''
    password = ""
    password_list = []
    for q in range(0, quantity):
        for i in range(0,value):
            c = random.choice(a)
            while c in password:
                c = random.choice(a)
            password += c
        password_list.append(password)
        password = ""
    return password_list


def show(a):
    print("-------------------------------------")
    for i in range(0, len(a)):
        print(f"password{i+1}: {a[i]}")
    print("-------------------------------------")


os.system("cls")
print("---------------------------------------")
print("Wellcome to strong password genarator.")
print("---------------------------------------")
while True:
    os.system("color 02")
    print("select the one of the items below:")
    print("1.Generate password")
    print("2.exit")
    print("---------------------------------------")
    item = input("select the item: ")
    if item == '1':
        os.system("cls")
        print("----------------------------------")
        print("NOTIC: your password must have more than 8 characters.")
        print("----------------------------------")
        value = int(input("Enter number of characters: "))
        quantity = int(input("Enter number of passwords you need: : "))
        #print(generate_password(value, quantity))
        show(generate_password(value, quantity))
    elif item == '2':
        break
    else:
        print("Invalid Item!")