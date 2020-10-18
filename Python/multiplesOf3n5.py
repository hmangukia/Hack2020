'''
This program lists all the multiples of 3 and 5 below n.
The input is taken from the user.
'''

def multiplesOf3n5(n):
    flag = 0
    for i in range(1, n):
        if (i % 3 == 0) and (i % 5 == 0):
            flag = 1
            print(i)
        else:
            continue
    if flag == 0:
        print("No multiple of 3 and 5 found!")

n = int(input("Enter a number: "))
if n < 5:
    print("Please enter a number greater than 4")
else:
    multiplesOf3n5(n)
