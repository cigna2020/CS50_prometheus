import csv

def survey():
    username = input('Enter your name: ')
    while not username.isalpha():
        username = input('Please try to enter your name again: ')

    userage = input('Enter your age: ')
    while not userage.isnumeric():
        userage = input('Please try to enter your age again: ')

    useraddress = input('Enter your address: ')
    while not useraddress.isalnum():
        useraddress = input('Please try to enter your address again: ')


    file = open('register.csv', 'a')
    writer = csv.writer(file)
    writer.writerow((username, userage, useraddress))
    file.close()

survey()