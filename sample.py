print("=====Devguard AI =====")
password = input("enter your password: ")
score = 0
if len(password) >= 8: score += 1
if any(c.isupper() for c in password): score += 1
if any(c.islower() for c in password): score += 1
if any(c.isdigit() for c in password): score += 1
if any(not c.isalnum() for c in password): score += 1
print("score:", score, "/5")
if score <= 2: print("strength: weak")
elif score <= 4: print("strength: medium")
else: print("strength: strong")
print("scan completed!")
