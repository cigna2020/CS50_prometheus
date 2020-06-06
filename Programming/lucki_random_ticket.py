from random import randint

def generate_ticket_number():
    return randint(0, 999999)

def is_ticket_lucky(num):
    num = str(num)
    num = '0' * (6 - len(num)) + num
    return int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5])

def get_ticket():
    number = generate_ticket_number()
    is_valid = is_ticket_lucky(number)
    return (number, is_valid)


my_ticket_in_bus = get_ticket()
if my_ticket_in_bus[1] == True:
    template = 'Woohoo! I\'m lucky, my ticket is %s'
else:
    template = 'My ticket is %s. Will try tomorrow.'
print(template % (my_ticket_in_bus[0]))