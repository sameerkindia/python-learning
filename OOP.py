# # OOP

# class PlayerCharacter():
#     playerTotal = 0
#     def __init__(self, name):
#         self.name = name

#     def run(self, score=1):
#         # print(f'{self.name} run')
#         self.playerTotal += score
#         return f'{self.name} score {score} run {self.playerTotal}'


# playerSameer = PlayerCharacter('sameer')
# playerSahil = PlayerCharacter('sahil')


# # print(playerSameer.name)
# # print(playerSahil.run(2))
# # print(playerSahil.run(3))
# # print(playerSahil.run(4))
# # print(playerSahil.run(6))
# # print(playerSahil.run(6))
# # print(playerSahil.run(6))
# # print(playerSahil.run(6))

# # class newPlayer:
# #     def __init__(self):
# #         pass

# #     def run(self):
# #         return self
    

# # runPlayer = newPlayer()
# # methodRun = runPlayer.run()

# # print(methodRun.run())


# # Inheritance

# class User():
#     def log_in(self):
#         print('logged in')

# class Wizard(User):
#     def __init__(self, name , power):
#         self.name = name
#         self.power = power
    
#     def attack(self):
#         print(f'{self.name} attack with {self.power} power')

# class Archer(User):
#     def __init__(self,name,power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'{self.name} attack with {self.power} power')


# wizard1 = Wizard('tong' , 33)
# wizard2 = Wizard('garo' , 75)

# archer1 = Archer('cj' , 55)
# archer2 = Archer('tomy' , 67)

# archer1.attack()
# archer1.log_in()

# wizard1.attack()
# wizard2.attack()



# How to create a class in python?
# What is __init__
# Abstarction 
# Incapculation
# Inheritance
# Polymorphisam

class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self, city=''):
        if city :
            print(f'Hello, my name is {self.name}, I am {self.age} years old and I live in {city}')
            return
        
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

class Leader(People):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def hello(self):
        self.intro()
        print(f'hello leader')


sameer = People('sameer' , 25)
sahil = People('sahil' , 27)

sk = Leader('Sameer khan', 25 , 'Web developer')

print(sameer.name)
print(sameer.age)
sameer.intro()
sahil.intro('pali')

sk.intro()
sk.hello()