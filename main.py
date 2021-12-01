import random

letters = ['a','b','c','d','e','f','g','h','i','j','k',
'l','m','n','o','p','q','r','s','t','u','v','w','x','y'
,'z','A','B','C','D','E','F','G','H','I','J','K','L',
'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


########## EASY LEVEL #############

password = "" # Variable to store the password

for char in range(1, nr_letters+1):
    password += random.choice(letters)

for char in range(1,nr_symbols+1):
    password += random.choice(symbols)

for char in range(1,nr_numbers+1):
    password += random.choice(numbers)

print(f"\nThis is our easy password: {password}")



########## HARD LEVEL #############

hard_password = list(password)
nr_password = int(len(password))

print(f"\nThis is whats inside the hard password: {hard_password}")


shuffle_list = random.shuffle(hard_password)
final_pass = ''.join(map(str, hard_password))

print(f"\nThis is our final reassembled password: {final_pass}")
