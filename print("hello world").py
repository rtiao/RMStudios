# print("hello world")
# first_name = "Ryan"
# last_name = "Tiaokhiao"
# full_name = first_name +" "+last_name
# print("Hello "+ full_name)
# print("Hello "+full_name)
#
# age = 25
# age = age + 2
# age += 1
# print(age)
# print(type(age))
#
# height = 250.5
# print("Your heig)ht is: "+str(height)+"cm"
# print(type(height))
#
# human = False
# print(human)
# Data types

    # 1. Variables = a container for a value. Behaves as the value that it contains.
    # 1. String = a series of characters.
        # 1. to create a string you can either use single or double quotations.
    # 2. Int = integer
        # 1. when you assign a value with the int data type, do not use quotes (would technically be a string).
        # 2. If you need to display a variable of a different data type along w/ string, use stringcast to convert data type to string
    # 3. float = floating point number (decimal number)
        # 1. a numeric value that can store a number that includes a decimal.
            # 1. Int data types cant store decimals
    # 4. boolean = datatype that can only store true or false

# multiple assignments = allows us to assign multiple variables at the same time in one line of code

# name = "ryan"
# age = 25
# attractive = True

# name, age, attractive = "ryan", 25, True
#
# print(age)
# print(name)
# print(attractive)

    # string method no.4

# name = "Ryan"

# print(len(name))
#print(name.find("r"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count('o'))
# print(name.replace("a","i"))
# print(name*3)

    # no. 5 type casting
# type casting = convert the data type of a value to another data type
#
# x = 1 #int
# y = 2.0 #float
# z = "3" #str

# x = str(x)
# y = str(y)
# z = str(z)

# print("X is "+str(x))
# print(y)
# print(z*3)

    # no.6 user input
# when accepting a use input it is always a str data type

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input("How tall are you?: "))
#
# # sports = input("What is your favorite sports team?: ")
# # print("Hello "+ name + " go "+ sports + "!")
#
# print("Hello "+name)
# print("You are "+str(age)+" years old")
# print("You are "+str(height)+"in tall")

    # no.7 math functions
# import math

# pi = 3.14
# x = 1
# y = 2
# z = 3

# print(round(pi)) = rounds to the nearest int.
# print(math.ceil(pi)) = rounds up
# print(math.floor(pi)) = rounds down
# print(abs(pi)) = absolute value of no.
# print(pow(pi,2)) = exponent ie. 2
# print(math.sqrt(pi)) = sq root function
# print(max(x,y,z)) = finds the largest int
# print(min(x,y,z)) = finds the smallest int

    # no. 8 string slicing
# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#             [start:stop:step]
# step = the amount increased via index

# name = "Ryan Tee"

# first_name = name[:4] = prints "ryan"
# last_name = name[5] = prints "T"
# funky_name = name[:8:2]
# reveresed_name = name[::-1]

# print(reveresed_name)

# website1 = "http://google.com"
#
# website2 = "http://wikipedia.com"
#
# slice = slice(7,-4)
#
# print(website1[slice])
# print(website2[slice])
#
    # NO.9 If statements

# age = int(input('How old are you?: '))
#
# if age == 100:
#     print("You are hella old ngl")
#
# elif age >= 18:
#     print('You are UNC status :(')
#
# elif age < 0:
#     print('You are a lil ah boi')
#
# else:
#     print('You are YN status :)')

    #NO.10
# logical operators (and,or,not) = used to check if two or more conditional statements are true

# temp = int(input("What is the temperature outside?: "))
#
# if not(temp >=0 and temp <= 30):
#     print('It is hot af')
#     print('Turn on the a/c')
#
# elif not(temp < 0 or temp) > 30:
#     print('The temperature is good today')
#     print('Go touch grass')
#     print('It is hot af')
#     print('Turn on the a/c')
    #NO.11
# while loop = a statement that will execute it's block of code,
#                           as long as it remains true

# name = None
# while not name:
    # name = input('Enter your name: ')

# print("GOOD BOY "+name)

    #NO.12 For Loops
# for loop = a statement that will execute it's
    # block of codde a limited amount of times

        #while loop = unlimited
        #for loop = limited

# for i in range(10):
#     print(i+1)

# for i in range(50,100+1,2):
    # print(i)

# for i in ("Ryan Tiaokhiao"):
    # print(i)

#creating a for loop that will countdown
#import time

#for seconds in range(10,0,-1):
    #print(seconds)
 #   time.sleep(1) # the rate at which in decreases in
#print('Happy New Year!')
