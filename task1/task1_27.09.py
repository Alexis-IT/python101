import random
from statistics import mean

list_of_numbers = [random.randint(0,1000) for i in range(100)]

list_of_numbers.sort()
average_even = average_odd = sum_of_even = count_of_even = 0
list_of_odd = list_of_numbers.copy()

for i in list_of_numbers:
    if i%2 == 0:
        sum_of_even = sum_of_even + i
        count_of_even = count_of_even + 1
        list_of_odd.remove(i)

if count_of_even == 0:
    print("Even numbers didn't find")
else:
    average_even = sum_of_even/count_of_even
    print('average_even = ', average_even)

if count_of_even == len(list_of_numbers):
    print("Odd numbers didn't find")
else: 
    average_odd = mean(list_of_odd)
    print('average_odd = ', average_odd)

