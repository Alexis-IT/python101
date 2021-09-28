import random
from statistics import mean
from collections import Counter


def enter_number():
    check = False

    while check == False:
        print('Please, enter lenght of list:')

        try:
            n = int(input())
            check = True
            if n<=0:
                print('You should enter only integer number greater than 0')
                check = False
        except Exception:
            print('You should enter only integer number')
            check = False   
    return n

def sorted_random_list(n):
    list_n = [random.randint(0,1000) for i in range(n)]
    list_n.sort()
    return list_n



def get_list_of_even(list_of_numbers):
    inner_even_list = []
    for i in list_of_numbers:
        if i%2 == 0:
            inner_even_list.append(i)
    return inner_even_list


def get_list_of_odd(list_of_numbers1,list_of_numbers2):
    diff = Counter(list_of_numbers1)
    diff.subtract(Counter(list_of_numbers2))
    return list(diff.elements())

  
def main():
    average_even = average_odd = 0
    list_lenght = enter_number()
    user_list_of_numbers = sorted_random_list(list_lenght)
    list_of_even = get_list_of_even(user_list_of_numbers)
    list_of_odd=get_list_of_odd(user_list_of_numbers,list_of_even)

    '''
    #uncoment this part for check lists

    print('sort list:', user_list_of_numbers)
    print('even part:', list_of_even)
    print('odd part', list_of_odd)
    '''

    if len(list_of_even) == 0:
        print("Even numbers didn't find")
    else:
        average_even = mean(list_of_even)
        print('average_even = ', average_even)

    if len(list_of_even) == len(user_list_of_numbers):
        print("Odd numbers didn't find")
    else: 
        average_odd = mean(list_of_odd)
        print('average_odd = ', average_odd)

if __name__ == '__main__':
    main()

