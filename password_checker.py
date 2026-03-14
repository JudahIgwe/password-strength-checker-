import re

def check_password(password):
    score = 0
    if len(password) >= 8:
        score = score + 1
    if re.search(r'[A-Z]', password):   
        score = score + 1
    if re.search(r'[a-z]', password):
        score = score + 1
    if re.search(r'[0-9]', password):
        score = score + 1
    if re.search(r'[^a-zA-Z0-9]', password):
        score = score + 1
    if score <= 2:
        return "Weak password"
    elif score == 3:
        return "Medium password"
    else:
        return "Strong password"
        
password = input("Enter a password to check: ")
print(check_password(password))
