"""grade = input("Enter your grade : ")
if grade == 'A' or grade ==  "a":
    print("your average score is 19")
elif grade == "B" or grade == "b":
    print("your average score is 16")
elif grade == "C" or grade ==  "c":
    print("your average score is 12.5")
elif grade == "F" or grade ==  "f":
    print("your average score is below 10-")
else:
    print("please enter a correct grade")
    """


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


number = int(input("Enter your number:"))
result = 0
for i in range(1,number):
    if number % i == 0:
        result += i
        
if result == number:
    print("your number is prime ")
else:
    print("your number is not prime")