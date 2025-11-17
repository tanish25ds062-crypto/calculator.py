@@ -0,0 +1,521 @@
print("hloooooo")
print("hello world") 
if 5 > 2:
    print("five is greater than two")

print("hello")
x = 5
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
#how to comment 
#cbxcjkbsdbc
#;klvhsdjovgvbsvlskdbvs
#VARIABLE TYPES ::
x = 69
y = "hello"
print(type(x)) 
print(type(y))


x = 4.9
print(type(x))

#BOOLIAN
x = 5
y = 4
print(bool(x + y))
print(bool(x))



my_var = 40
print(my_var)


x,y,z = "40","50", "60"
x = "40","50", "60" #it works as array
print(x)


fruits = ["apple", "banana","cherry"]
x=y=z = fruits
print(type(x))
print(x)


fruits = [2,3,4,5,6]
print(type(fruits))


x = "good"
y = "is"
z = "python"
print(z,y,x)

x = "good"
def my_function():
    print("python is "+x)
    my_function()
my_list = ["apple","banana",1,3,5,7]

my_list[2:5]="abc"

print(my_list)

my_list= [1,2,4,5,6]

my_list.insert(2,3)
print(my_list)

my_list.insert(2,"add any word")
print(my_list)
my_list.append("add in last")
print(my_list)
my_list.remove("add any word")
print(my_list)

list1 = [1,2,3]
list2 = [4,5,6]

list1.extend(list2)
print(list1)

list3=[1,2,3,"apple",4,5]
list3.pop(3) #pop means remove
print(list3)

list3.clear()
print(list3)
list3= ["hello"]
print(list3)
list3.append(1)
print(list3)

# loops list 
list1=[1,2,3,4,4,4,5,6]
for x in list1:
    print(x)

#sort 
list = [2,5,1,4,8]
list.sort() #asscending order 
print(list)
list.sort(reverse=True) #desscending order
print(list)



my_list = ["apple","banana",1,3,5,7]
my_list[2:5]="abc"
print(my_list)



my_list= [1,2,4,5,6]
my_list.insert(2,3)
print(my_list)

my_list.insert(2,"add any word")
print(my_list)
my_list.append("add in last")
print(my_list)
my_list.remove("add any word")
print(my_list)

list1 = [1,2,3]
list2 = [4,5,6]

list1.extend(list2)
print(list1)

list3=[1,2,3,"apple",4,5]
list3.pop(3) #pop means remove
print(list3)

list3.clear()
print(list3)
list3= ["hello"]
print(list3)
list3.append(1)
print(list3)

# loops list 
list1=[1,2,3,4,4,4,5,6]
for x in list1:
    print(x)

#sort 
list = [2,5,1,4,8]
list.sort() #asscending order 
print(list)
list.sort(reverse=True) #desscending order
print(list)



text ="hello Python"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("Python", "world"))
print(text.split())


# format string
name = "Alice"
age = 20
print(f"my name is {name} and i am {age} years old")

name = "Bob"
age = 25
print(f"my name is {name} an dim {age} years old")
  

  #using % formatting (older method)
name = "Charlie"
age = 30
print("my name is %s and i am %d years old." %(name , age))

#assing operrator

x = 5
x-= 2
print(x)
x+= 3
print(x)
x/= 2
print(x)
x%= 2
print(x)
x**= 2
print(x)
x//= 2
print(x)



#comparisosn operators
x = 10
y = 7

print(x>y)
print(x==y)
print(x<y)
print(x>=y)
print(x<=y)
print(x!=y)


#logical operator 
x = 5
print(x > 3 and x < 10)
print(x > 3)


#identity operator
x = [1,2,3]
y = x 
z = [1,2,3]
print(x is y)
print(x is z)

# Python Tuples
# A tuple is an orderd collection of items , similar to a list , but cannot be change 
number = (1,2,3,4,5)
print(number)


# python sets {}
colors = {"red", "green", "blue"} 
print(colors)
# Adding elements 
colors.add("yellow")
print(colors)
#Removing elements
colors.remove("green")
print(colors)
# Iterating through set 
for color in colors:
    print(color)

#data types
x = 5
print(type(x))

x = "5.6"
print(type(x))

x = "good"
print(type(x))

x = 5.6
print(type(x))


#list 
my_list = ["apple", "banana"]
print(type(my_list))
print(my_list)

print(len(my_list))

my_list = ["apple", "banana", "cherry", "khfhgxg", "jhcfhgcx", "hvjhccg"]
print(my_list[0])
print(my_list[0:2])
print(my_list[0:1 ])
print(my_list[-4:-1])


# creating dictonary 
student = {"name":"aamir", "age":"19","grade":"A"}
print(student)
print(type(student))

#accessing Values
print(student["name"])
print(student["age"])

#adding/ updating value 
student ["age"] =21
student ["city"] = "Gurgoan:"
print(student)

# removing items
student.pop("grade")
del student["city"]
print(student)

#Iterating through 
for key, value in student.items():
    print(key,":",value)
   
age = 20 


if age >= 18:
 print("you are eligible to vote.")
else:
 print("you are not eligible for vote")
 
age = 17
if age < 18:
 print("you are not eligivble for vote ")
else:
 print("you are eligible for vote")

#if else

age=20

if age>=18:
  print ("you are adult")

elif age==18:
  print("you are teen")

elif age==17:
  print("you are 17")

elif age==16:
  print("you are 16")

else:
  print("you are not adult")


m=18
n=1
z=m+n
print(z)
a=15
if(a%2!=0):
    print("the number is odd")
else:
    print("the no. is even")

# number to print positie and negative number 
a=12
z=a*-1

if(z<0):
    print("number is positive",a)
else:
    print("number is negative")

    # OR
a=15
if(a>0):
    print("number is positive ")

else:
    print("number is negative")

for i in range(1,4):
    for j in range(1,3):                    # run this code untill it ends the condition of j
        print(f"i={i},j={j}")       

for i in range(1,6):
    if i==4:
        break
    print(i)



for i in range(1,6):
    if i==4:
        continue
    print(i)

def greet(name):
  print(f"hello,{name}!")
greet("Alice")
greet("Bob")

for i in range(1, 21):
    print(i)
for i in range(2, 30, 2):
    print(i)
def grret():
    print("hello world")

grret()
def add(a,b):
    return a+b
result=add(5,3)
print(result)
x=10
def my_fxn():
    y=5
    print("inside:",x,y)
my_fxn()
print("outside:",x)
def greet():
    print("Hello!")

# Call the function
greet()
 
def add_numbers():
    # This version asks for input instead of taking parameters
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a + b

result1 = add_numbers()
print(result1)
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid number!")

print(f"You entered: {number}")

# Age validation example
while True:
    try:
        age = int(input("Enter your age (0-120): "))
        if 0 <= age <= 120:
            break
        else:
            print("Please enter a valid age between 0 and 120")
    except ValueError:
        print("Please enter a valid number!")

print(f"Valid age entered: {age}")
# Class

class Car:
    def __init__(self, brand, color):  # Fixed: double underscores and proper spacing
        self.brand = brand  # Attribute
        self.color = color  # Attribute

    def drive(self):  # Method
        print(f"{self.color} {self.brand} is driving ")  # Fixed: self.color instead of self color

# Objects
car1 = Car("BMW🚔🏍🚗", "Black")
car2 = Car("Tesla", "White")

car1.drive()
car2.drive()

import array
numbers=array.array("i",[1,2,3,4,5])
print(numbers)

#numpy

from numpy import random
x=random.randint(100)
print(x)

x=random.rand()
print(x)
print(x)
print(type(x))

'''[54] # 0-D array

[1,2,3,4] # 1-D array

[[1,2,3]  # 2-D array
 [4,5,6]]

[[[1,2,3]    # 3-D array
  [4,5,6]]
  [[7,8,9]
   [5,3,6]]]'''     #show blocks

from numpy import random
x=random.randint(100,size=(3,5))    #(3,5) row,column
print(x)

x=random.randint(100,size=(2,3,5))    # row,column
print(x)

x=random.randint(100,size=(2,2,3,5))    # row,column
print(x)

#generate random number from Array
from numpy import random
x = random.choice([3,4,5,8,7], size = (5))
print(x)
import pandas as pandas

data=[10,20,30,40]

s=pandas.Series(data)
print(s)



import pandas as pd 
data= {
  "Name":["Alice","Bob","Charlie","David"],

  "Age":[24,27,22,32],
  "City":["Delhi","Mumbai","Chennai","Kolkata"]
}

df=pd.DataFrame(data)
print(df)
import numpy as np 
arr= np.array([1,2,3,4,5])
a = pd.Series(arr)
print(s)

# from a dictonary

data = {"Math":90,"Science":85,"English":78}
s = pd.Series(data)
print(s)

import pandas as pd
df=pd.read_csv("Spotify_Youtube.csv.zip")
print(df.head())
print(df.tail)