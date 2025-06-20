import sys
import random

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
# print(num1 , num2)
# print(random.randint(num1,num2))
winning_num = random.randint(num1 , num2)


while True:
    try:
        user_num = int(input("guess my number :- "))
        if num1 <= user_num <= num2 :
         if user_num == winning_num:
            print(f'you are a genius my number is {winning_num}')
            break
        else: 
         print(f'{num1} se {num2} ke beach main batao')
    except ValueError:
        print('areee! number chahiye yaar')
        continue