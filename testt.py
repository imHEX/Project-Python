"""
Exercises:
1) از کاربر گرید بگیرید و بازه نمره او را تعیین کنید . 
2) برنامه ای بنویسید که 5 عدد از کاربر بگیرد و کوچکترین و بزرگترین آنها را چاپ کند
3) برنامه ای برای تشخیص کامل بودن عدد بنویسید .

"""


"""
variables: 
string, int, float, bool

condition:

if condition:
	body
else:
	body

"""

#if 3 > 20:
#    print("3 > 2")
#else:
#    print("bye bye")


print("-"*50)

"""
if condition1:
    body
elif condition2:
    body
elif condition3:
    body
    .
    .
    .
    .
else:
    body

"""

# day = int(input("please enter a number : "))
# if day == 1:
#     print("شنبه")
# elif day == 2:
#     print("یک شنبه")
# elif day == 3:
#     print("دو شنبه")
# elif day == 4:
#     print("سه شنبه")
# elif day == 5:
#     print("چهار شنبه")
# elif day == 6:
#     print("پنج شنبه")
# elif day == 7:
#     print("فیتیله جمعه تعطیله...... ")
# else:
#     print("1 - 7 borto khonatooon")


# score = float(input("please enter  your score : "))
# if score > 17 and score <= 20:   # (17, 20]
#     print("you got A grade")
# elif score > 14 and score <= 17:
#     print("you got B grade")
# elif score >= 10 and score <= 14:
#     print("you got C grade")
# elif score >= 0 and score < 10:
#     print("you got F grade")

"""
Loop : حلقه
for i in sequence:
    body

list, string, range(start, end, step=1)
"""

#name = "mojtaba ghahri"
#for i in "mojtaba ghahri":
#    print(i)

#colors = ['crimson', "blue", "yellow", "blue", "green"]
#for color in colors:
#    print(color)

#print("-"*50)


# for i in range(10, 20):  # 0 1 2 3 4 5
#     print(i)

# 5! = 1*2*3*4*5    3! = 1*2*3     4!=11*2*3*4   1!= 1   0!= 1


# number = int(input("please enter a number : ")) # 5
# fact = 1 #range(1, 6)
# for i in range(1, number+1):     # 1     2    3     4   5     6
#     # fact = fact * i              # 1*1  1*2  2*3  6*4  24*5
#     fact *= i
# print(f"{number}! = {fact}")


# number = int(input("please enter a number : "))
# summ = 0
# for i in range(1, number + 1):
#     # summ = summ + i
#     summ += i

# print(summ)

# n1 = int(input("please enter a number : "))
# n2 = int(input("please enter a number : "))
# evens = []
# odds = []


# for i in range(n1, n2):
#     if i % 2 == 0:
#         evens.append(i)
#     else:
#         odds.append(i)
# print(evens)
# print(odds)


num = int(input("please enter a number : "))
flag = 0
for i in range(1, num):
    if num % i == 0:
        flag += i

if (flag == num):
    print(f"{num} is Prime")
else:
    print(f"{num} is not Prime")


#             0        1        2        3       4
#colors = ['crimson', "blue", "yellow", "blue", "green"]
#for i in range(0, len(color)):
#    print(colors[i])
