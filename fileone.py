"""
user_name = input("Enter Username\n")
password = input("Enter Password\n")
char = len(password)
encoded = char * '*'
print(f'Username: {user_name}, Your password is {encoded}, {char} characters long')

# CODE1
my_list = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

i, j = 0, 0
fill = '*'
empty = ' '

while i <= 5:

    pass

    while j <= 6:
        # if is executed on truth
        if my_list[i][j]:
            print(fill, end='')
        else:
            print(empty, end='')
        j += 1
    print('')
    i += 1
    j = 0


# CODE2
# Checking duplicates in the list'

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for values in some_list:
    if some_list.count(values) > 1:
        if values not in duplicates:
            duplicates.append(values)
print(duplicates)

# CODE3
# Print highest even
def highest_even(li):
    evens = []
    for values in li:
        if values % 2 == 0:
            evens.append(values)
    return max(evens)


print(highest_even([11, 2, 3, 4, 8, 10]))


# CODE 4
# Scope

a = 1 #Global scope


def parent():
    a = 10

    def confusion():
        return a

    return confusion()


print(parent())
print(a)

# 1. Start with local
# 2. Parent local?
# 3. Global
# 4. Built in python functions

# CODE 5
# Object Oriented Programming
# Objects and classes



class PlayerCharacter:
    # Class Object Attribute or class variable or static variable
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name  # attributes or instance variable
            self.age = age

    @classmethod
    def sumofnum(cls, age):
        return age
    def agesum(cls,num1,num2)
        return cls('teddy', num1+num2)


    @staticmethod
    def cat(name):
        return name

Player3 = PlayerCharacter.agesum(2,3)
Player1 = PlayerCharacter('Ravi', 20)
Player2 = PlayerCharacter('Sam', 10)

print(f'Players names are {Player1.name} & {Player2.name}')
print(f'Players age are {PlayerCharacter.sumofnum(22)} & {PlayerCharacter.sumofnum(21)}')
print(PlayerCharacter.cat('samy'))




# Code 6
# Inheritance

class SignIn:
    def Login(self):
        print('Signed-in')


class Cars(SignIn):

    def __init__(self, name):
        self.name = name
        print(f'Car name is {self.name}')

    def Audi(self):
        print('We are Cars')

    def Engine(self):
        print('200 HP')


class Bikes(SignIn):
    def __init__(self, name):
        self.name = name
        print(f'Bike name is {self.name}')

    def Kawaski(Self):
        print('We are bikes')

    def Engine(self):
        print('100 HP')


Car1 = Cars('BMW')
Bike1 = Bikes('Kawaski')

print(Car1.Login())


# isinstance which checks if some object is an instance of class
# Super() method



# Code 7
# Dunder Methods

class Toy:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.mydict = {
            'Name': 'Aditya',
            'Roll': 32
        }

    # Overwritten Dunder Method
    def __str__(self):
        return f'Color name is {self.name}'

    def __del__(self):
        return print('Deleted!')

    def __call__(self):
        return ('Yess')

    def __getitem__(self, i):
        return self.mydict[i]


obj1 = Toy('Red', 1)

print(str(obj1))
print(obj1.__str__())
print(obj1())
print(obj1['Roll'])
del obj1


# Code 8
# Extending list

class SuperList(list):
    def __len__(self):
        return 1000


List = SuperList()

print(len(List))
List.append(5)
print(List[0])
print(issubclass(SuperList,list))

# Method resolution order (MRO)
# Use __mro__ or use .mro() method to know the order



# Code 9
# Functional Programming
# map(),filter(), zip(),reduce()

# Map will run the function multiply_by_2 for us and loops all items in iterable and returns for us a new map object
# that we convert into our list
my_list = [1, 2, 3, 4, 5]
your_list = [10, 20, 30, 40, 50]


def multiply_by_2(item):
    return item * 2


print(list(map(multiply_by_2, my_list)))
print(my_list)


# filter()

def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)

# zip(),  combine items together

print(list(zip(my_list, your_list)))

# reduce
from functools import reduce


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list,0))


# Code 10
# Lambda Expressions (used for one time , when have a function is used once)
# lambda param : action on (param)

# Square
my_list2 = [2, 3, 4]
print(list(map(lambda squared: squared ** 2, my_list2)))

# List-Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
sort_second = lambda lt: lt[1]
a.sort(key=sort_second)
print(a)

# List Comprehensions

my_li = [char for char in 'hello']
my_li2 = [num for num in range(0, 100)]
my_li3 = [num ** 2 for num in range(0, 100)]
my_li4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

# Set & Dict Comprehensions
# {} set comprehension use curly braces
my_dict1 = {number: number * 2 for number in [1, 2, 3]}

simple_dict = {'a': 1, 'b': 2}
my_dict2 = {k: v ** 2 for k, v in simple_dict.items()}

print(my_dict1)
print(my_dict2)


# Code 11
# Set has no duplicate elements

some_list1 = ['a','b','a','c','d','e','b','f']

duplicates1 = list(set([x for x in some_list1 if some_list1.count(x) > 1]))

print(duplicates1)



# Code 12
# Higher order functions are those accept function as a parameter and return function
def greet(func):
    func()


def greet2():
    def func():
        return 5

    return func()


# Code 13
# Decorator, we can decorate patterns functions, and add functionality o the functions

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*****')
        func(*args, **kwargs)
        print('*****')

    return wrap_func


@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('Hi emoji')


# Code 14
# Decorator 2

from time import time


def performance(fn):
    def wrapped_fn(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)

        t2 = time()
        print(f'it took {t2-t1} seconds to complete')
        return result

    return wrapped_fn


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()


# Code 14
# Error Handling
# try, except, else block

while True:
    try:
        age = int(input('What is your age?'))
        10/age
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print("Please enter the age higher than '0' ")

    else:
        print('Thank You!')
        break

#Code 15
def sum(num1, num2):
    try:
        return num1/num2
    except(Type error, ZeroDivisionError) as err:
        print(err)
    finally:
        print("I am done")

print(sum(1, '2')

# for own error use
# raise ValueError('hey, custom error raised')

# Code 15
# Python generators are a simple way of creating iterators
# Generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
# Generators - generators are Iterable , not everything that is iterable is a generator ex: range is iterable but not a
# list
# Any object in python which can be iterated over is iterable

def generator_function(num):
    for i in range(num):

        yield i*2  # yield pause the function


obj1 = generator_function(1000)
print(next(obj1))
print(next(obj1))
print(next(obj1))



# Code16
# Modules in python

# Organizing code, importing methods from other files in python, the files in python are modules
# A Package is a folder that contains modules, package is a folder and modules are files in that are in the package

# import filename
# import package-name.filename
# from filename import 'function1 name','functions2name'
# from package.subpackage import filename
# from package.subpackage.filename import 'functions'
# if __name__=='__main__':  >>  __name__ is the file(module) name, but file which import everything is __main__ file
    do this


# Code 16
# Random game

# Check if the number is a right guess , Otherwise
# Ask again

from random import randint
import sys

# Generate a number from 1-10
answer = randint(int(sys.argv[1]),int(sys.argv [2]))

while True:
    try:
        # Input from User
        guess = int(input('Guess a number from 1~10:   '))

        # Check that input is a number 1-10

        if 0 < guess < 11:
            if guess == answer:
                print('You guessed it right')
                break
        else:
            print('I told you to enter between 1~10')

    except (ValueError):
        print('Enter a number')
        continue

"""
# Code 17
# Translator


