"""
Exercises:

1) جدول ضرب 9*9
2) رسم لوزی با کاراکتر ستاره
3) دو عدد از کاربر گرفته و اعداد اول ما بین دو عدد را یافته ، درون یک لیست ذخیره کنید .
4) برنامه ای بنویسید که یک عدد از کاربر گرفته و تعیین کند کامل است یا خیر، با استفاده از حلقه 
while
5) با استفاده از حلقه for
برنامه ای بنویسید که یک عدد از کاربر گرفته و به تعداد آن عدد جمله سری فیبوناچی تولید کند . 
6) برنامه ای بنویسید که یک عدد از کاربر بگیرد و مغلوب آن را چاپ کند
"""


# minimum = None
# maximum = None

# for i in range(5):
#     num = int(input("please enter a number : "))
#     if minimum == None:
#         minimum = num
#         maximum = num
#     else:
#         if num < minimum:
#             minimum = num
#         if num > maximum:
#             maximum = num
# print(f"minimum = {minimum}\nmaximum = {maximum}")


# numbers = [20, 9, 7, 8, -3, 56, -45, 0 ,15]
# print(numbers)
# print(min(numbers))
# print(max(numbers))

# numbers.sort()
# print(numbers)
# print(numbers[0])
# print(numbers[-1])


"""
nested Loop: حلقه تو در تو

"""

# fname = "mojtaba"
# lname = "ghahri"


# print(fname, end=' ')

# print(lname)

num = 8
for i in range(num):            # 0 1 2
    for j in range(num):        # 0 1 2 3
        print("*", end=" ")  # * * * 
    print()                   # * * *

print("-"*50)


for i in range(1, 6):
    for j in range(i):
        print("*", end=" ") 
    print()
print("-"*50)

for i in range(5):
    for j in range(5 - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ") 
    print()

print("-"*50)

for _ in range(5):
    print(f" {_} Hello world!")

print("-"*50)




"""


"""

for i in range(5):
    for j in range(5):
        print("*", end=" ")

    print()


"""
while 

"""

for i in range(0, 5, 1):
    print(i)

print("-"*50)

i = 0         # 0
while i < 5:  # T T T T T F
    print(i)  # 0 1 2 3 4
    i += 1    # 1 2 3 4 5

# while False:
#     print("Hello world!")


# 5! = 1*2*3*4*5    3! = 1*2*3

# num = int(input("please enter a number : "))
# fact = 1
# i = 1
# while i <= num:
#     fact *= i
#     i += 1

# print(f"{num}! = {fact}")


number = int(input("please enter a number : "))
flag = 0
i = 2
while i < number:
    if number % i == 0:
        flag += 1
    i += 1

# if flag == 0:
#     print(f"{number} is prime")
# else:
#     print(f"{number} is not prime")

numbers = []

while len(numbers) < 10:
    numbers.append(num)
    num = int(input("please enter a number : "))

print(numbers)
