import random
print("Welcome to password generator!")
letters=['a','f','g','r','y','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['#','@','^','*',')',"%"]
numbers=["0",'1','2','3','4','5','6','7','8','9']
n_letters=int(input("Enter how many letters do you want?"))
n_symbols=int(input("Enter how many numbers of symbols you want?"))
n_numbers=int(input("enter how many numbers of numbers you want?"))
password_list=''
for i in range(1,n_letters+1):
  out=random.choice(letters)
  password_list+=out
for i in range(1,n_symbols+1):
  out=random.choice(symbols)
  password_list+=out
for i in range(1,n_numbers+1):
  out=random.choice(numbers)
  password_list+=out
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for i in password_list:
  password+=i
print(password)
  