def string_loop(string_1):
    # string_1 = "venugopal"
    start_index = 0
    end_index = len(string_1)
    while start_index < end_index:
        print(string_1[start_index],end=" ")
        start_index=start_index+2
    # for i in range(start_index,len(string_1)-1,2):
    #     print(string_1[i],end=" ")
#
# def str_loop():
#     string_2 = "newzealand"
#     start = 0
#     end = len(string_2)
#     while start < end:
#         print([start],end=" ")
#         start = start + 1

# def string_new(new):
#     start = 0
#     end = len(new)
#     for i in range(start,len(new)):
#         print(new[i],end=" ")

# def product():
#     i=1
#     prod=1
#     for i in range(1,11):
#         prod = prod * i
#         print(prod)

# def total():
#     i = 1
#     addition = 0
#     for i in range(1,11):
#         addition = addition+i
#         print(addition)

# def address(name,age):
#     print(name,age)
#
# def student(name, age):
#     print('Student Details:', name, age)
# student("pony","29")

# def add(a,b):
#     print(a-b)

def percentage(*args):
    total = 0
    for i in args:
        total = total + i
    avg = total / len(args)
    print("average is =", avg)

def marks(*subjects):
    total = 0
    for i in subjects:
        total = total + i
    average_marks = total/len(subjects)
    print("the % scored is = ", average_marks)

def for_factorial(end_index):
    factorial = 1
    for start_index in range(1, end_index+1):
        factorial = factorial * start_index
    print(" the fact is ", factorial)

def while_factorial(num):
    factorial = 1
    start_index = 1
    while start_index <= num:
        factorial = factorial * start_index
        start_index = start_index + 1

def find_fact(num):
    factorial = 1
#     start_num = 1
#     while start_num <= num:
#         factorial = factorial * start_num
#         start_num = start_num + 1
#     print(" the factorial is = ",factorial)
#
# def fact_test(n):
#     factorial = 1
#     for i in range(1,n):
#         factorial = factorial * n
#     print("the factorial is ", factorial)
#
# # def str_access(place,skip_index):
# #     start = 0
# #     end = len(place)
# #     while start < len(place):
# #         if start != skip_index:
# #             print(place[start],end= " ")
# #             start = start + 1
#
# def str_access(place,skip_index):
#     for i in range(0,len(place)):
#         if i != skip_index:
#             print(place[i], end=" ")

# def prime_num(num):
#     for i in range(2,num):
#         if num % i == 0:
#             print()

# def grammer(word):
#     vowels = 0
#     consonant = 0
#     for i in range(0,len(word)):
#         if word[i] in ["a","e","i","o","u"]:
#             vowels = vowels + 1
#
#         else:
#             consonant = consonant + 1
#     print(vowels, "are the vowels")
#     print(consonant,"are the consonants")
# def check_prime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True
#
# def twin_prime(num):
#     for first_num in range(2,num):
#         second_num = first_num + 2
#         if (check_prime(first_num) and check_prime(second_num)):
#             print("{0} and {1}".format(first_num,second_num))

# def fact(x):
#     factorial = 1
#     start_num = 1
#     while start_num <= x:
#         factorial = factorial * start_num
#         start_num += 1
#     print("the factorial is", factorial)

# def find_vc(word):
#     vowels = 0
#     conso = 0
#     for i in range(0,len(word)):
#         if word[i] in ["a","e","i","o","u"]:
#             vowels = vowels + 1
#         else:
#             conso = conso + 1
#     print("the vowels are ",vowels)
#     print("the conso are ",conso)

# def unique_bag():
# bag = [1,2,3,3,3,3,4,5,5,6,6,7,8,8]
# unique_bag = []
# for i in bag:
#     if i not in unique_bag:
#         unique_bag.append(i)
# print(unique_bag)
#
# def unique_bag():
#     bag= [1,2,3,3,3,3,4,5,5,6,6,7,8,8]
#     uni_bag = []
#     for i in bag:
#         if i not in uni_bag:
#             uni_bag.append(i)
#     print(uni_bag)

# def word_check(word):
#     vowels = 0
#     consonants = 0
#     for i in range(0,len(word)):
#         if word[i] in ["a","e","i","o","u"]:
#             vowels = vowels + 1
#         else:
#             consonants = consonants + 1
#     print("the total vowels in word is ",vowels)
#     print("the total consonants in word is ",consonants)

def check_prime(max_num):
    for i in range(2, max_num):
        if max_num % i == 0:
            return False
    return True


def twin_prime(max_num):
    for num_1 in range(2, max_num):
        num_2 = num_1 + 2
        if (check_prime(num_1) and check_prime(num_2)):
            print("{0} and {1}".format(num_1,num_2))



