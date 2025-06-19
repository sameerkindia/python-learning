# Decorators

# Python mein function ek first-class object hota hai. Iska matlab:
# Hum function ko ek variable mein assign kar sakte hai.
# Function ko ek function ke andar pass kar sakte hai.
# Function ke andar ek aur function bana sakte hai.
# Aur function se function return bhi kar sakte hai.


def greet():
    return "Hello!"

say_hello = greet  # function ko variable mein assign kiya
# print(say_hello())


# Function ke under function

def outer1():
    def inner():
        print("Yeh inner function hai")
    inner()

# outer1()


# Function se function return karna

def outer2():
    def inner():
        return "Inner se return"
    return inner

func = outer2()
# print(func())



# Function as a argument

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func):
    return func("Hello")

# print(speak(shout)) # speak function main humne shout function pass kiya
# print(speak(whisper)) # speak function main humne whisper function pass kiya







# -------------------------
# WHAT IS DECORATORS
# -------------------------

# Decorator ek function hota hai jo kisi doosre function ko leta hai, aur uske behavior mein kuch extra cheezein add karta hai — bina us function ko directly change kiye.


def decorator_function(original_function):
    def wrapper_function():
        print("Function se pehle kuch kar rahe hain...")
        print("Function se pehle kuch kar rahe hain...")
        print("Function se pehle kuch kar rahe hain...")
        return original_function()
    return wrapper_function

def say_hi():
    print("Hi!")

# Decorator ko call karne ke do tarike hai

# 1.
decorated = decorator_function(say_hi)
# decorated()

# 2. sahi tarika
@decorator_function
def say_helloji():
    print("Hello ji!")

# say_helloji()



# Agar function arguments leta ho? (Flexible Decorator)
# Humme pehle wrapper function main argument pass karne padenge

def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        print("Function call hone se pehle...")
        return original_function(*args, **kwargs)
    return wrapper

@decorator_function
def greet(name):
    print(f"Hello, {name}!")

# greet("Sameer")



# Hum ek saath do decorators ko bhi call kar sakte hai

def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def hello():
    print("Hello!")

# hello()


# Real-life use cases

# ✅ Logging – har function call ke baare mein print karwana
# ✅ Timing – function ko run karne mein kitna time laga
# ✅ Authentication – user allowed hai ya nahi
# ✅ Caching / Memoization – repeat calculations avoid karna
# ✅ Validation – arguments sahi hain ya nahi check karna


# Socho decorator ek gift wrapping jaisa hai 🎁 – gift wahi hai, lekin wrapping usko better bana deti hai.
# Socho ek mobile phone cover 📱 – cover lagane se phone ka asli function nahi badalta, lekin protection ya style add ho jata hai.



import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Function done")

# slow_function()

print(__name__ , 'from decorator')