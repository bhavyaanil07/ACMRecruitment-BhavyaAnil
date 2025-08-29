##PROBLEM 1
k=0
for i in range(1,1000,1):
    if i%3==0:
        k+=i
    elif i%5==0:
        k+=i
print('the sum of all the multiples of 3 or 5 below 1000 is ',k)
print('')


##PROBLEM 6
def sum_square_difference(n):
    sum_square = 0
    for i in range(1, n+1):
        sum_square += i**2
    sum_num = 0
    for i in range(1, n+1):
        sum_num += i
    square_sum = sum_num** 2
    difference = square_sum - sum_square
    return difference
print('THE DIFFERENCE IS ',sum_square_difference(100))
