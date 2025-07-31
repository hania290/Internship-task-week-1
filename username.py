name = input("Enter your full name: ")
name = name.strip()
parts = name.split()

if len(parts) >= 2:
    username = parts[0].lower() + '.' + parts[1].lower()
else:
    username = parts[0].lower()

print("Your username is:", username)
