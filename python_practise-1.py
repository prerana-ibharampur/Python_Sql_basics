# labequipments= ["beaker", "jar", "funnel", "pipette", "watch glass"]
# labequipments.insert(2, "burette")
# print(labequipments)
# labequipments.remove("jar")
# print(labequipments)
# labequipments.insert(-1, "burner")
# print(labequipments)
# labequipments.insert(len(labequipments), "dispenser")
# print(labequipments)
# labequipments.pop(-3)
# print(labequipments)


# L=[1,2,3,4,5]
# print("answer",L)
# L[0]=str(L[0])
# print(L)
# L[1]=str(L[1])
# print(L)
#
# a=int(input("your age"))
# print(a)
# b=str(input("your city"))
# print(b)
# c=float(input("your weight"))
# print(c)
# v=[1,2,3,4,5]
# v[0]=v[0]*5
# print(v)
# v[1]=v[1]*5
# print(v)
# v[2],v[3]=v[2]*5,v[3]*5
# print(v)
# a=int(input("type number_1"))
# b=int(input("type number_2"))
# if a ==b:
#     print("both the numbers are equal")
# else:
#     print("both the numbers are not equal")
#
# r=int(input("any number"))
# if r%2==0:
#     print(r, "is an even number")
# # else:
# #     print(r, "is not an even number")
# print("Program is completed")
# d=int(input("number"))
# if d%3==0:
#     print(d, "is divisible by 3")
# elif d%2==0:
#     print(d, "is divided by 2")
# else:
#     print(d, "is not divisible by 3")
# e = input("color")----------------------------------------------------imp
# e = e.strip()  # Removes any spaces before or after the input e
# #if e == "violet" or e == "indigo" or e == "blue" or e == "green":
# if e in ["violet", "indigo", "blue","green"]:
#     print(e, "is found in rainbow")
# elif e != "violet" and e != "indigo" and e != "blue" and e == "green":
#     print(e, " is not a color in rainbow")
# else:
#     print(e, " is a random color")
# n=int(input("write a number"))
# if n%5==0 and n%3==0:
#     print("fizzbuzz")
# elif n%5==0:
#     print("buzz")
# elif n%3==0:
#     print("fizz")
# else:
#     print("not fizzbuzz")
# g=[10,22,35]
# g[0], g[1], g[2] =g[0],g[1], g[2]
# print(g, "before multiplication")
# g[0],g[1], g[2] = g[0]*10, g[1]*10, g[2]*10
# print(g, "after multiplying by 10")
# g[-1]=g[-1]*30
# print(g)
# q=[1,2,3,4,5]
# q.insert(-1,(6))
# print(q)
# q.insert(-1,'7')
# print(q)
# q.insert(-3,9)
# print(q)
# q.insert(len(q),13)  # insert in last position
# print(q)
# r=[20,22,23,24]
# r.insert(1,21)
# print(r)
# r.insert(-2, 33)
# print(r)
# r.insert(len(r),65)
# print(r)
# a= 100
# b= 560
# if a > b:
#     print(a, "is greater than b")
# else:
#     print(b, "is greater than a")
# e=input("name the vehicle")
# if e in ['punch', 'nexon', 'creta','innova']:
#     print(e, "is a car")
# else:
#     print(e, "is not a car")
#
# r=input("name the object")
# if r=="table" or r=="chair" or r=="bench":
#     print(r, "is a wooden object")
# elif r!="table" and r=="chair" and r=="bench":
#     print(r, "is not a wooden object")
# else:
#     print(r, "is not an object")
# r="hello!"
# print(r)
# n=int(input("write a number")
# if n%2!=0:
#     print("Weird")
# elif n%2==0 and (n>=2 and n<5):
#     print("Not Weird")
# elif n%2==0 and (n>=6 and n<20):
#     print("Weird")
# elif n%2==0 and (n>20):
#     print("Not Weird")

# txt="Hello World"
# print(txt[:-1])

# fruits= ["orange","kiwi","apple"]
# fruits= [fruits.upper]

# s='simple'
# print(s[0])
# print(s[2], s[4])
# ACCESSING CHARACTERS OF A STRING==========================
# name= 'Venugopal'
# print(name[0]), print(name[3])
# print(name[1])
# print(name[0],name[1])
# print(name[0],name[2])
# print(name[2],name[-2])
# print(name[-2], name[-3], name[-4])
# n_2= ['Ibharampur']
# print(n_2[0])
# print(n_2[0][1])
# print(n_2[0][0])
# print(n_2[0][3])
# print(n_2[0][4],n_2[0][6])
# print(n_2[:])
# print(n_2[0][5],n_2[0][7])
# l=['a', 'b',[9,10,11,(1,2,3)]]======================excercise
# print(len(l))
# print(l[2][2])
# l=[['p','q'],['r','s'], 'prerana']
# print(len(l))
# print(l[1][1])
# l=((1,2,3),('p','q'))
# print(len(l))
# print(l[0][2])
# l=[[['s','t'], 'a','b'],('c','d')]
# print(len(l))
# print(l[1][0])

# names=['tiny','feet','home']
# print(names)
# for index in range(len(names)):
#     names[index] = names[index].upper()
#     print(names)
# # print(names)
# ============================================================================================================
# test = input('give a number ')
# test = int(test)
# factorial = 1
# while (test > 0):
#     factorial = factorial * test
#     test = test-1
# print('the factorial of the given number is' ,factorial)

# test_2 = input('enter a number ')
# factorial = 1
# test_2 = int(test_2)
# while (test_2 > 0):
#     factorial= factorial * test_2
#     test_2 = test_2-1
# print('the fact is ' , factorial)

# t = input('enter a number ')
# t= int(t)
# factorial = 1
# while (t > 1):
#     factorial = factorial * t
#     t = t -1
# print('the factorial of the given number is ', factorial)

# nums = [1,2,3,4,5]
# for num in nums:
#     print(num)

# test = [1,4,6,8,0]
# for num in test:
#     if num == 0:
#         print('found')
#     break
# print(num)

# nums = [1,2,3,4,5]
# for num in nums:
#     if num == 3:
#         print('found')
#         break
#     print(num)

# nums = [4,5,6,7]
# for num in nums:
#     if num == 7:
#         print('found')
#         break
#     print(num)

# bets = ['a','e','i','o','u']
# for pointer in bets:
#     if pointer == 'o':
#         print('found it')
#         break
#     print(pointer)

# def check_animal_in_list():
#     animals = ['cow', 'ant', 'deer', 'camel']
#     for i in animals:
#         if i == 'cow':
#             print('animal found', i)
#             break
#         print(i)
#         return

# check_animal_in_list()
from gramener_test import count_character as count_character
#   hbgbbb

# Checking for conflict

# def add(a,b):
#     c= a+b
#     return c
# a=10
# b=12
# print(c)

# def factorial(num):
#     if num.isdigit() and int(num)>0:
#         num= int(num)
#         fact= 1
#         while num > 0:
#             fact= fact * num
#             num=num-1
#         print('the factorial is' ,fact)
#     else:
#         print('invalid')
# factorial('6')

# am = 'cat'
# i=am[::-1]
# print(i)

# def greet():
#     print('hello')
# greet()

# def factorial(num):
#     if num.isdigit() and int(num)>0:
#         num= int(num)
#         fact = 1
#         while num > 0:
#             fact= fact * num
#         print('the factorial is ' , )
#     else:
#         print('invalid')
# factorial('7')

# def factorial(x):
#     x= int(x)
#     if x > 0:
#         d= 1
#         while x > 0:
#             d= d*x
#             x= x-1
#             print('the factorial is ',x)
#     else:
#         print('not valid')
# factorial(7)

# def add(a,b,c,d,e):
#     sum=(a+b+c+d+e)
#     print('the sum is',sum)
#     return sum
# add(8,2,3,0,7)

# def multiply(a,b,c,d,e):
#     product=(a*b*c*d*e)
#     print('the product is: ', product)
#     return product
# multiply(8,2,3,-1,7)

# def reverse_string(r_s):
#     r_s=""
#     print('the reversed string is',r_s)
#     return r_s
# r_s("1234abcd")

# a="0123456789"
# print(a[1:7:1])
# print(a[:7:1])
# print(a[::1])
# print(a[::-1])

# def reverse_string(a):
#     return a[::-1]
# b= str(input('enter'))
# c=reverse_string(b)
# print(c)

# def reverse(string):
#     reverse_string=""
#     for i in string:
#         reverse_string= i+ reverse_string
#     print("resversed string is: ", reverse_string)
# string= input('enter')
# print('entered string is', string)
# reverse(string)

# def reverse_string(r_s):
#     r_s=""
#     for i in r_s:
#         string_reverse= i+string_reverse
#     print('reversed string is: ',string_reverse)
# r_s= "venugopal"
# print('the given string is ', r_s)
# reverse_string(r_s)

# def check_if_in_range(A):
#     if A in range(1,10):
#         print(A ,'is in the given range')
#     else:
#         print('not in the given range')
# check_if_in_range(7)

# def check_range(x):
#     if x in range(1,100):
#         print(x, "is in the given range")
#     else:
#         print(x,'not in range')
# check_range(29)

# def unique_list(U):
#     n_list=[]
#     for alp in U:
#         if alp not in U:
#             n_list.append(alp)
#             return n_list
# print(unique_list, 'is n_list')
# unique_list([1,2,3,4,4,4,4,5,6,6,7])

# def unique_list(l):
#     x = []
#     for a in l:
#         if a not in x:
#             x.append(a)
#             return x
# print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))

# def factorial():
#     num= input('enter: ')
#     num= int(num)
#     if num > 0:
#         fac= fac*i
#         i=num-1
#         return fac
#         print('the factorial is ', fac)
# factorial()


# print('hello, my name is prerana,', end=" ")
# print('I\'m from Karnataka')

# e=100.3
# i=25
# t=(e+i)
# print(t)

# e=float("100.3")
# i=float("25")
# t=(e+i)
# print(t)

# name=input()
# print('you have entered')
# print(name)

# name=input("what is your name ")
# age= input("enter your age ")
# print(f"your name is {name}")
# print(f"your age is {age}")

# first= input("enter num_1 ")
# sec= input("enter num_2 ")
# sum= int(first)+ int(sec)
# print(sum)

# WAP TO FIND AREA OF A RECTANGLE
# length= float(input("Enter the length "))
# width= float(input("Enter the width "))
# area= length * width
# print("the area of rectangle is ",area)
# print(f"the area of the rectangle is {area}")

# WAP TO FIND THE AVG OF THREE NUMBERS
# num_1=input("Enter the first number ")
# num_2=input("Enter the second number ")
# num_3=input("Enter the third number ")
# num_1=int(num_1)
# num_2=int(num_2)
# num_3=int(num_3)
# sum=num_1+num_2+num_3
# avg_num=sum/3
# print("the average is ",avg_num)

# num=55.5
# num=int(num)
# print(num)

# WAP TO CONVERT TEMP IN FAHRENHEIT TO CELSIUS
# temp=input("Enter the temp F ")
# temp=int(temp)
# celsius= (temp-32)* 5/9
# print("the temp in celsius is ", celsius)

# WAP TO FIND SUM OF 5 SUBJECTS AND FIND PERCENTAGE
# kan=int(input("k.marks= "))
# eng=int(input("e.marks= "))
# math=int(input("m.marks= "))
# sci=int(input("sci.marks= "))
# social=int(input("s.marks= "))
# total=(kan+eng+math+sci+social)
# percentage= total/5*100
# print("your percentage is ",percentage)

# WAP ASK NUMBER OF GAMES PLAYED . ASK THE USER NUMBER OF GAMES WON AND NUMBER OF GAMES LOST.
# CALCULATE NUMBER OF TIE AND TOTAL POINTS.(1 WIN=4 POINTS,1 TIE=2 POINTS)
# game=int(input("how many games have you played? "))
# game_won= int(input("how many won? "))
# game_lost= int(input("how many lost "))
# tie= game-game_won-game_lost
# print("games_tied= ",tie)
# total_points= (game_won*4)+(game_lost*2)
# print("total points= ", total_points)

# f_d=-10//4
# print(f_d)

# # ASSIGNMENT OPERATORS:
# x=10
# x=x+5
# print(x)
#
# y=20
# y+=5
# print(y)

# LOGICAL OPERATORS
# phy=int(input("enter physics marks "))
# chem=int(input("enter chemistry marks "))
# print(phy>33 and chem>33)
# print(phy>33 or chem>33)

# num1= input("enter first number ")
# num2=input("enter second number ")
# if num1>num2:
#     print(num1, "is greater")
# else:
#     print(num2,"is greater ")

# num_1= int(input("enter 1st number"))
# num_2= int(input("enter 2nd number"))
# if num_1 > num_2:
#     print("num_1 is greater")
# else:
#     print("num_2 is greater")

# num= int(input("enter "))
# if num % 2==0:
#     print("even number")
# else:
#     print("odd number")

# phy= input("enter physics marks ")
# chem= input("enter chem marks ")
# if int(phy)>35 and int(chem)>35:
#     print("PASS")
# else:
#     print("FAIL")

# num= input("enter ")
# num=float(num)
# if num>=0:
#     print("positive interger")
# else:
#     print("negative integer")

#WAP TO PRINT LAST DIGIT IN ANY NUMBER:
# digit= int(input("enter "))
# last_d= digit%10
# # print(f"the last digit is {last_d}")
#

# number= input("enter a number ")
# number=int(number)
# last_digit= number%10
# if (last_digit)/5==0:
#     print(f"the last digit is {last_digit} and it is divisible by 5")
# else:
#     print("NO")

# WAP USING NESTED IF-ELSE:
# num= input("enter ")
# if num.isdigit() and int(num)>=0:
#     if int(num) >0:
#         print("positive")
#     else:
#         print("equal to zero")
# else:
#     print("negative")

# i=1
# while i<=20:
#     print(i,end=" ")
#     i = i + 1

# n=1
# while n<=20:
#     if n!=16 and n!=18:
#         print(n, end=" ")
#     n=n+1

# name="karnataka"
# for i in range(0,len(name)):
#     if name[i]!="k":
#         print(name[i],end="")
#
# while i in range(0,len(name)):
#     if name[i]!="a":
#         print(name[i],end)

# i=1
# while i<=10:
#     print(i,end="")
#     i=i+1

# i=1
# while i<=30:
#     if i%2==0:
#         print(i, end=" ")
#     i=i+1

# num=2
# while num<=30:
#     print(num, end=" ")
#     num=num+2

# WAP ASK A NUMBER FROM USER. PRINT ALL THE NUMBERS FROM 1 TO THAT NUMBER

# num=input("enter a number ")
# num=int(num)
# i=1
# while i<=num:
#     print(i,end=" ")
#     i=i+1

# num=input("enter ")
# num=int(num)
# i=1
# while i<=num:
#     print(i, end=" ")
#     i=i+1

# WAP ASK  A NUMBER.PRINT ALL NUMBERS FROM N TO 1.
# num=input(" enter a number ")
# num= int(num)
# i=num
# while i>=1:
#     print(i, end=" ")
#     i=i-1

# first=int(input("enter "))
# end=int(input("enter "))
# i=first
# while i<=end:
#     print(i,end=" ")
#     i=i+1

# wap to find the sum of all numbers from 1 to 10
# num=1
# total=0
# while num<=10:
#     total=total+num
#     num=num+1
# print(total)

# i=1
# total=0
# for i in range(1,11):
#     total=total+i
#     i=i+1
# print(total)

# i=1
# product=1
# for i in range(1,11):
#     product=product*i
#     i=i+1
# print(product)
#
# j=1
# product=1
# while j<=10:
#     product=product*j
#     j=j+1
# print(product)
# from python_functions import string_loop as string_loop
# string_loop("sheela")
# # print("\n")
# string_loop("australia")
#
# from python_functions import string_new as string_new
# string_new("united")
# from python_functions import total as total
# total()
# from python_functions import address as address
# address("Venu","31")
#
# from python_functions import student as student
# # student("timpu","2")
# student(age="10",name="rama")
#
# from python_functions import while_factorial as marks
# marks(4)
# from python_functions import str_access
# str_access("uttarakhand",4)
# from python_functions import grammer
# grammer("australia")
# from python_functions import twin_prime
# twin_prime(1000)
# from python_functions import fact
# fact(5)
# from python_functions import find_vc
# find_vc("temperature")

# from python_functions import unique_bag
# unique_bag()
#
# +++
# +++++++++++++++++++++"']]'"

# letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#
# find_1 = input("enter the number ")
# new = int(find_1) % 26
# print(letters[new - 1])
# from python_functions import word_check
# word_check("glaceir")
# from python_functions import twin_prime
# twin_prime(800)

# for pat in range(5):
#     print("*" * pat)
# for pat in range(6):
#     x = "*"
#     x = x * pat
#     print(f'{x: ^10}')

# OOPS PRACTISE
# class Student:
#     def __init__(self,name):
#         self.name = name
# stu1 = Student("Pinky")
# print(stu1.name)

# PUBLIC (ACCESS MODIFIERS)
# class Account:
#     def __init__(self,acc_num,acc_pass):
#         self.acc_num = acc_num
#         self.acc_pass = acc_pass
#
# acc = Account("12345","ghjk")
# print(acc.acc_num)
# print(acc.acc_pass)

# PRIVATE ACCESS MODIFIER
# class Account:
#     def __init__(self,acc_num,acc_pass):
#         self.__acc_num = acc_num
#         self.__acc_pass = acc_pass
# acc = Account("789456","plkj")
# print(acc.__acc_num)

# class Car:
#     color = "red"
#     @staticmethod
#     def start():
#         print("car started")
#     @staticmethod
#     def stop():
#         print("car stopped")
# class Tatacar(Car):
#     def __init__(self,name):
#         self.name = name
# car1 = Tatacar("Tiago")
# car2 = Tatacar("Nexon")
# print(car2.stop())
# print(car1.start())
# print(car1.color)
# class Punch(Tatacar):
#     def __init__(self,type):
#
#         self.type = type
# car3 = Punch("Petrol")
# car3.start()
# MULTIPLE INHERITANCE
# class A:
#     var = "Welcome to class A"
# class B():
#     var = "Welcome to class B"
# class C(A,B):
#     pass
#     # var = "Welcome to class C"
# c1 = C()
# print(c1.var)
# print(c1.var)
# print(c1.var)

# PRORERTY DECORATOR
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+ "%"
# stu1 = Student(56,85,94)
# print(stu1.percentage)
# stu1.phy = 86
# print(stu1.percentage)

# POLYMORPHISM
#  Complex:
#     def __init__(self,real,img):
#         class self.real = real
#         self.img = img
#
#     def show_num(self):
#         print(self.real, "i +",self.img,"j")
#     def total(self,num1):
#         new_real = self.real + num1.real
#         new_img = self.img + num1.img
#         return Complex(new_real,new_img)
#
# num1 = Complex(2,5)
# num1.show_num()
# num2 = Complex(7,9)
# num2.show_num()
# num3 = num1.total(num2)
# num3.show_num()

# LAMBDA FUNCTION
# lambda arguments: expression
# num = lambda a: a+10
# print (num(7))
#
# num_1 = lambda e,f : e*f
# print(num_1(8,9))
#
# from python_functions import my_new_fun
# from python_functions import new_exp
# num_1 = input("enter a number ")
# num_2 = input("enter a number ")
# try:
#     divide = int(num_1) / int(num_2)
#     print(divide)
# except ZeroDivisionError as e:
#     print("it was an error")
# except:
#     print("it was an error")
# else:
#     print("no errors")
# finally:
#     print("the program ends")

# lis = (1,2,3,4,1,1,2,3)
# set_lis = list(set(lis))
# for ele in set_lis:
#     [ele] = lis.count(ele)
#
# from python_functions import check_palindrome
# # word = ""
# check_palindrome("grammer")
# check_str = input("enter a word ")
# if check_str.isalpha() and check_str.islower():
#     print("TRUE")
# else:
#     print("FALSE")
