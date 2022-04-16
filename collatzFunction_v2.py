#Collatz sequence function, v2
    #improve try-except user-experience when enter non-integer number
    #cleaner global and local variable separation (num & number)
    #reduce collatz() function code line
    #cleaner (easier read) separate out input-number code block from calling collatz() function code block.

#one parameter, if even number, function evaulates to parameter // 2 (floor divide by 2)
# if parameter's odd number, function returns 3 * parameter + 1
# allow user to type in an integer, and then keep calling function until returns value of 1.

def collatz(num):               #create function, given a parameter, num
    if num % 2 == 0:            #if num is even, print & return num // 2
        num = num // 2
    elif num % 2 == 1:          #if num is odd, print & return 3*num+1
        num = 3*num+1
    print(num)
    return num
    
print("Enter an integer: ")     #ask user to submit a number, repeat if there's an error
while True:
    try:                        # try-except in case user enter non-intenger input
        number = int(input())
        break                   #input's good, no need to re-enter
    except ValueError:
        print("Please enter an integer")    #re-submit input (continue w/ while loop)

while True:              #keep calling collatz() until it returns 1
        number = collatz(number)    #call collatz(), note: collatz() will print its result
        if number == 1:             #stop while loop when collatz() returns 1
            break

