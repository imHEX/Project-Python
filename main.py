# grade = input("Enter your grade : ")
# if grade == 'A' or grade ==  "a":
#     print("your average score is 19")
# elif grade == "B" or grade == "b":
#     print("your average score is 16")
# elif grade == "C" or grade ==  "c":
#     print("your average score is 12.5")
# elif grade == "F" or grade ==  "f":
#     print("your average score is below 10-")
# else:
#     print("please enter a correct grade")



#num1 = int(input("please enter your first number:"))
#num2 = int(input("second number:"))
#num3 = int(input("third number:"))
#num4 = int(input("fourth number:"))
#num5 = int(input("fith number:"))
#numbs = [num1,num2,num3,num4,num5]
#numbs.sort()
#print(f"the highest number is {numbs[-1]}")
#print(f"the lowest number is {numbs[0]}")


#lowest = numbs[0]
#highest = numbs[0]
#for i in numbs:
#    if i < lowest:
#        lowest = i
#    elif i > highest:
#        highest = i
#print (f"the highest number is {highest}")
#print(f"the lowest number is {lowest}")


# number = int(input("Enter your number:"))
# result = 0
# for i in range(1,number):
#     if number % i == 0:
#         result += i
        
# if result == number:
#     print("your number is prime ")
# else:
#     print("your number is not prime")


# list1 =[1, 5, 50, 3, 8, 90]
# index8 = list1.index(8)
# list1[index8] = 80
# print(list1)


# num = [10,20,[300,400,[5000,6000],500],30,40]
# num[2][2].append(7000)
# print(num)

# num = input("enter your number:")
# fa = "۰۱۲۳۴۵۶۷۸۹"
# result = ""
# for i in num:
#     result += fa[int(i)]
# print(result)

#1)

# for i in range(4):
#     for j in range(4 - i):
#         print(" ", end=" ")
#     for j in range(2 * i - 1):
#         print("*", end=" ")
#     print()
# for i in range(2, 0, -1):
#     for j in range(4 - i):
#         print(" ", end=" ")
#     for j in range(2 * i - 1):
#         print("*", end=" ")
#     print()

#2)

# for i in range(1,10):
#     for j in range(1,10):
#         print(i * j, end="\t" )
#     print()
    
#3)
    
# num1 = int(input("first number:"))
# num2 = int(input("second number:"))
# if num1 > num2 :
#     num1, num2 = num2, num1

# for n in range(num1, num2 + 1):
#     is_prime = n >= 2
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#     if is_prime:
#         print(n)


#4)

# number = int(input("Enter your number:"))
# result = 0
# i = 1 
# while i < number:
#     if number % i == 0:
#         result += i
#     i += 1
    
# if number > 1 and result == number:
#     print(number, "your number is prime ")
# else:
#     print(number, "your number is not prime")

#5)

# num = int(input("enter number:"))
# a = 0
# b = 1
# for i in range(num):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

#6)

# num = input("enter number:")
# numlist = list(num)
# numlist.reverse()
# for i in numlist:
#     print(i, end="")