#Collatz sequence function
#one parameter, if even number, function evaulates to parameter // 2 (floor divide by 2)
# if parameter's odd number, function returns 3 * parameter + 1
# allow user to type in an integer, and then keep calling function until returns value of 1.

def collatz(num):               #create function, given a parameter, num
    if num % 2 == 0:            #if num is even, print & return num // 2
        print(number // 2)
        return number // 2
    elif num % 2 == 1:          #if num is odd, print & return 3*num+1
        print(3*number+1)
        return 3*number+1
    
print("Enter number: ")     #ask user to enter a number
try:                        # try-except in case user enter non-intenger input
    number = int(input())
    while True:              #keep calling collatz() until it returns 1
        number = collatz(number)    #call collatz(), note: collatz() will print its result
        if number == 1:             #stop while loop when collatz() returns 1
            break
except ValueError:
    print("Please re-run program & enter an integer")



