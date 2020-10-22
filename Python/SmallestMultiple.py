'''
This program gives the smallest number that is divisible by all the numbers till n,
here n should be less than 50 and greater than 0.
'''
import copy

def smallestMultiple(n):
    multiple = copy.copy(n)
    boolVal = True
    while boolVal:
        flag = 0
        print(multiple)
        for i in range(1, n):
            if multiple % i == 0:
                continue
            else:
                flag = 1
                multiple = multiple + n
                break

        if flag == 0:
            print("The smallest number divisible by 1 to {} is {}".format(n, multiple))
            boolVal = False

n = int(input("Enter a number: "))
if n < 1 or n > 50:
    print("Please enter a number between 1 and 50")
else:
    smallestMultiple(n)
