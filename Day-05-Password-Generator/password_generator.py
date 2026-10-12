import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["1","2","3","4","5","6","7","8","9","10"]
symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|',]

#first easy level
"""
password = ""

harf = int(input("Oluşturmak istediğiniz şifrede kaç tane harf olsun? "))
sayi = int(input("Oluşturmak istediğiizi şifrede kaç tane sayı olsun? "))
sembol = int(input("Olsuşturmak istediğiniz şifrede kaç tane sembol olsun? "))
for asd in range(1,harf+1):
    password +=  random.choice(letters)
for asd in range(1,sayi+1):
    password += random.choice(numbers)
for asd in range(1,sembol+1):
    password += random.choice(symbols)
print(password)
"""

#hard level


harf = int(input("Oluşturmak istediğiniz şifrede kaç tane harf olsun? "))
sayi = int(input("Oluşturmak istediğiizi şifrede kaç tane sayı olsun? "))
sembol = int(input("Olsuşturmak istediğiniz şifrede kaç tane sembol olsun? "))

password_list = []

for asd in range(1,harf+1):
    password_list.append(random.choice(letters))
for asd in range(1,sayi+1):
    password_list.append(random.choice(numbers))
for asd in range(1,sembol+1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""

for asd in password_list:
    password += asd
print(f"İşte yeni ve güçlü şifreniz: {password}")
