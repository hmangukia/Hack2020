'''
This program gives the sum of the digits of the factorial of n.
'''

def SumOfFactorial(n):
    factorial = 1
    sum = 0
    for i in range(1, n+1):
        factorial = factorial * i

    for j in str(factorial):
        sum = sum + int(j)

    print("The sum of digits of factorial of n is ", sum)

n = int(input("Enter a number: "))
if n < 1:
    print("Please enter a number greater than 0")
else:
    SumOfFactorial(n)
