'''
This program finds the sum of square
of first n natural numbers.
Input is obtained from the user.
'''

def SumOfSquares(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i * i
    return sum

def SquaresOfSum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return (sum * sum)

n = int(input("Enter a number: "))
if n < 1:
    print("Please enter a number greater than 0")
else:
    ans = SquaresOfSum(n) - SumOfSquares(n)
    print("The difference between square of sums and sum of squares of first {} natural numbers is {}".format(n, ans))
