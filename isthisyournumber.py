import random
x = int(input('write your minimum value : '))
y = int(input('write your maximum value : '))

number = random.randint(x,y)
number = int(number)
print(number)
HOL = input('is this your number?(Yes/Higher/lower)')
while HOL != "Yes":
    if HOL == "Higher":
       x = number+1
       number = random.randint(x, y)
    elif HOL == "Lower":
       y = number
       number = random.randint(x, y)
    print(number)
    HOL = input('is this your number?')
print("YOU SUCK!")
