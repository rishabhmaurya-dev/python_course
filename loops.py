# print 1 to 10 numbers

# for i in range(1,11):
#   print(i)

# /////////////////////////////////////dz

# print 1 to 100 all odd numbers

# for i in range(1,101,2):
#   print(i)

# //////////////////////////////////////

# print 1 to 100 all even numbers

# for i in range(0,101,2):
#   print(i)

# /////////////////////////////////////

# print 5 ka table

# n = 5
# for i in range(1,11):
#   print(f"{n} * {i} = {n*i}")

# ////////////////////////////////////

# sum of n natural numbers

# n = 5
# sum = 0
# for i in range(1,n+1):
#   sum += i
# print(sum)

# ////////////////////////////////////

# factorial of number

# n = 5
# fact = 1
# for i in range(1,n+1):
#   fact *= i
# print(fact)

# ////////////////////////////////////

# print all characters of string in reverse order

# str = "saurabh maurya"
# rev = ""
# for char in str:
#   rev = char + rev
# print(rev)

# ////////////////////////////////////

# sum of all list elements 
# lst = [1,2,3,4,5]
# sum = 0
# for i in lst:
#   sum += i
# print(sum)

# ////////////////////////////////////

# return max elem in a list

# lst = [1,4,340,56,34]
# max = lst[0] 
# for i in lst:
#   if i > max:
#     max = i

# /////////////////////////////////////

# return min elem in a list

# lst = [131,23,340,56,34]
# min = lst[0] 
# for i in lst:
#   if i < min:
#     min = i
# print(min)

# //////////////////////////////////////

# string me vowels count 

# str = "saurabh"
# vowels = 0
# for i in str:
#   if i in ["a","e","i","o","u","A","E","I","O","U"]:
#     vowels += 1
# print(vowels)

# /////////////////////////////////////////////////////

# list me even ki alag list aur odd ki alag list cretae KeyError

# lst = [1,2,3,4,5,65,7,8,8885,534,54,6,7]
# odd = []
# even = []
# for i in lst:
#   if i % 2 == 0:
#     odd.append(i)
#   else:
#     even.append(i)
# print(odd)
# print(even)

# ///////////////////////////////////////////////

# check prime number

# num = int(input("Enter the number : "))
# factor = 0
# for i in range(1,num+1):
#   if num % i == 0:
#       factor += 1
# if factor == 2:
#   print("Prime number")
# else:
#   print("Not a prime number")

# ///////////////////////////////////////////////

# list me duplicate number Find

# lst = [1,2,2,3,4,3,4,2]
# dup_list = []
# for i in lst:
#   if lst.count(i) >= 2:
#     if i not in dup_list:
#       dup_list.append(i)
# print(dup_list)

# //////////////////////////////////////////////

# count frequency of string characters

# str = "rcsdcc"
# for i in str:
#   print(i," = ",str.count(i))

# ////////////////////////////////////////////////////

# lst = ["rishabh","anish",1 ,"raj"]

# for i in enumerate(lst,start=0):
#   print(list(i))

# ///////////////////////////////////////////////

#  multiplication table grid

# for i in range(1,11):
#   for j in range(1,11):
#     print(f"{i*j}")

# ////////////////////////////////////////

# reverse string

# str = "rishabh"
# print("".join(reversed(str)))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# print(str[::-1])

# ////////////////////////////////////////

# string me digits count

# str = "rish2abh123"
# count = 0
# for i in str:
#   if i >= "0" and i <= "9":
#     count += 1
# print(count)
# ......................................
# str = "rish2abh123"
# count = 0
# for i in str:
#   if i.isdigit():
#     count += 1  
# print(count)

# ////////////////////////////////////////

# Count spaces
# str = "rish abh 123"
# count = 0
# for i in str:
#   if i == " ":
#     count += 1
# print(count)

# ////////////////////////////////////////