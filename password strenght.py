password = input('set a password: ')
has_upper = False
has_lower = False
has_digit = False
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    else: 
        has_digit = True

strenght= has_upper + has_lower + has_digit
if len (password) <6:
    print ('your password is weak')
elif strenght==4:
    print ('strong password')
else:
    print ('weak password')
