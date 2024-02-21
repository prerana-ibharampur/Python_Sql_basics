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

# animals = ['cow', 'ant', 'deer', 'camel']
# for i in animals:
#     if i == 'cow':
#         print('animal found', i)
#         break
#     print (i)


#hbgbbb

# Checking for conflict

















