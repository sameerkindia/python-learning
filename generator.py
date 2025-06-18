# Generator 

import time

def performance(func):
    def wrapper():
        start = time.time()
        # print('something before')
        # print('something after')
        func()
        end = time.time()

        print(f"total time {end - start} seconds")
    
    return wrapper


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Use the generator
counter = count_up_to(5)
# for number in counter:
#     print(number)


def generate_primes():
    n = 2
    while True:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n
        n += 1

# Get first 10 prime numbers
primes = generate_primes()
# for _ in range(10):
#     print(next(primes))


def febonachi(n):
    a = 0
    b = 1

    for _ in range(n):
        yield a

        temp = a
        a = b
        b = temp + b


@performance
def febo():
    for feb in febonachi(2000000):
        # print(feb)
        pass

@performance
def feboList():
    a = 0
    b = 1

    febArr = []

    for _ in range(2000000):
        febArr.append(a + b)

        temp = a
        a = b
        b = temp + b

    return febArr

febo()
feboList()

# @performance
# def hello():
#     print('hello ji')


# hello()