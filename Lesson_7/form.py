import csv

username = input('Enter your name: ')
userage = input('Enter your age: ')
useraddress = input('Enter your address: ')

file = open('register.csv', 'a')

writer = csv.writer(file)
writer.writerow((username, userage, useraddress))
file.close()
print(str(file))