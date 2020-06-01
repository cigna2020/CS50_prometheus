import csv

def survey():
    username = input('Enter your name: ')
    while username.isdigit():
        print('Please try to enter your name again: ')
        username = input('Enter your name: ')

    userage = input('Enter your age: ')
    while userage.isalpha():
        print('Please try to enter your name again: ')
        userage = input('Enter your age: ')

    useraddress = input('Enter your address: ')

    file = open('register.csv', 'a')
    writer = csv.writer(file)
    writer.writerow((username, userage, useraddress))
    file.close()

survey()