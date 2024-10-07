with open("account.txt", "r+") as file:
    lines = file.readlines()
    balance = lines[0].split(";")[1]
print(lines)
print(balance)