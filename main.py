# import decorators
from pyjokes.jokes_de import neutral

from decorators import timer
import time
from shopping import shopping_cart
import random
import pyjokes

joke = pyjokes.get_joke("en" , "neutral")

print(joke)
# print(decorators.timer)
# print(timer)

@timer
def slowFunc():
    time.sleep(3)
    print('learning module with timer')


# slowFunc()
# print(__name__)
print(shopping_cart.my_cart)
shopping_cart.add_to_cart('apple')
shopping_cart.add_to_cart('ball')
shopping_cart.add_to_cart('cards')
shopping_cart.add_to_cart('pin')
print(shopping_cart.my_cart)


# print(random.randint(1,10))