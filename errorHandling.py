# Error aur Exception kya hota hai?
#  Error = Jab Python interpreter kisi problem mein atak jata hai.

#  Exception = Error ka woh form jisko hum handle (control) kar sakte hain.



# try-except ka basic

# try:
#     x = int(input("Enter a number: "))
#     print(10 / x)
# except ZeroDivisionError:
#     print("Zero se divide nahi kar sakte!")
# except ValueError:
#     print("Please ek valid number dalo.")



# else clause
# Agar try block mein koi error nahi aata, toh else run hota hai:
try:
    x = 5
    y = 2
    result = x / y
except ZeroDivisionError:
    print("0 se divide nahi hota!")
else:
    print("Sab sahi chala, result:", result)


# finally clause
# Chahe error aaye ya na aaye — finally hamesha run hota hai. Mostly cleanup ke liye use hota hai 
try:
    x = 5
    y = 2
    result = x / y
except ZeroDivisionError:
    print("0 se divide nahi hota!")
else:
    print("Sab sahi chala, result:", result)
finally:
    print("Main to har haal main chalunga chahe error ho ya na ho")



# Custom Exception banana
# Apne khud ke errors bana sakte hai — jaise validations ke liye:

class AgeTooSmallError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeTooSmallError("Tum abhi chhote ho!")
    else:
        print("Entry allowed.")

try:
    check_age(16)
except AgeTooSmallError as e:
    print("Custom Exception:", e)




# Multiple Exceptions handle karna

try:
    a = int("abc")
    b = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print("Error :", e)




# Nested try-except

try:
    x = int(input("Enter a number: "))
    try:
        result = 10 / x
        print(result)
    except ZeroDivisionError:
        print("0 se divide nahi kar sakte.")
except ValueError:
    print("Please number input karo.")