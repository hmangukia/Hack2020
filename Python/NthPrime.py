'''
This program finds the sum of the square of first n natural numbers
'''

def SumOfSquares(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i * i

    print("The sum of squares of first {} natural numbers is {}".format(n, sum))

n = int(input("Enter a number: "))
if n < 1:
    print("Please enter a number greater than 0")
else:
    SumOfSquares(n)
