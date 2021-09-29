import random
from statistics import mean
from collections import Counter


def enter_number():
    '''Validate entered numbers

    Checks whether the input is an integer number greater than 0.
    Warning user if it is not true and asks to write the number again.
    '''
   
    check = False

    while check == False:
        print('Please, enter lenght of list:')

        try:
            n = int(input())
            check = True
            if n<=0:
                print('ATTENTION: You should enter only integer number greater than 0. \n')
                check = False
        except Exception:
            print('ATTENTION: You should enter only integer number. \n')
            check = False   
    return n

def sorted_random_list(n):
    ''' Create sorted list which lenght is "n". Elements of list are integers numbers.'''

    list_n = [random.randint(0,1000) for i in range(n)]
    list_n.sort()
    return list_n



def get_list_of_even(list_of_numbers):
    ''' Get list of even numbers from input list of integer numbers.'''

    inner_even_list = []
    for i in list_of_numbers:
        if i%2 == 0:                             # check if number is even
            inner_even_list.append(i)
    return inner_even_list


def get_list_of_odd(list_of_numbers1):
    ''' Get list of odd numbers from input list.'''

    diff = Counter(list_of_numbers1)                              # Create dictionary with  the count of each element
    diff.subtract(Counter(get_list_of_even(list_of_numbers1)))    # From generated list exclude elements which are even
    return list(diff.elements())

  
def run():
    '''The main function'''
    
    average_even = average_odd = 0
    list_lenght = enter_number()
    user_list_of_numbers = sorted_random_list(list_lenght)
    list_of_even = get_list_of_even(user_list_of_numbers)
    list_of_odd=get_list_of_odd(user_list_of_numbers)

    # # Uncoment these parts for show:
    #print('sort list:', user_list_of_numbers)   # generated list 
    #print('even part:', list_of_even)           # list of even elements from generated list
    #print('odd part', list_of_odd)              # list of odd elements from generated list

    # Cath cases when even/odd numbers don't exist in list
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
    run()

