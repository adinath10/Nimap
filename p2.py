n = int(input())
value = input()[:n]

sp,d,ucase,lcase = 0,0,0,0

for i in range(len(value)):
    if (ord(string[i]) >= 97 and ord(string[i]) <= 122):
            lcase += 1

        # For upper letters
    elif (ord(string[i]) >= 65 and ord(string[i]) <= 90):
            ucase += 1

    elif(i.isdigit()):
            d = d+1

    else:
            sp+=1

print("password contains:")
print("special character ", sp)
print("Digits :", d)
print("upper ", ucase)
print("lower ", lcase)
