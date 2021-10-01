import random
from random import randint   # Why need write this part? with import random - doesn't work


# Q1 How much pairs should exist in dict?
# Q2 Should dict's have the same numbers of pairs?
# Q3 (with using random) Does Py automaticly filer value of keys if they aready exists?
# Q4 What code shoul return as result?



def generate_random_dict():

    numb_pairs = random.randint(2,5)             # How much pairs should exist in dict?
    
    key_values=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    inner_dict= { key_values[randint(0, 25)]: randint(0, 100) for i in range(numb_pairs)}
    
    # # Alternative way for generate list of dict

    # import string
    # inner_dict= {choice(ascii_lowercase): randint(0, 100) for i in range(numb_pairs)}

    
    return inner_dict


def list_of_dict():
    
    n = random.randint(2,10)
    list_of_random_dict = [generate_random_dict() for i in range(n)]
    
    return list_of_random_dict

def dictionary_from_list(inner_list):
    inner_dict_list = {}
    for dict_from_list in inner_list:
        for x, y in dict_from_list.items():
            inner_dict_list[x]=y

    new_dict={}
    for dict_from_list in inner_list:
        for k, v in dict_from_list.items():
            for w, z in inner_dict_list.items():
                if w == k and v > z:
                    new_dict[k] = v                   # HERE SHOULD BE CODE !!!!!!!!!!!! 
                else:
                    new_dict[w] = z
                
    return new_dict




def run():
    generated_list_of_dict = list_of_dict()
    print(generated_list_of_dict, '\n')
    print('generated_list_of_dict:', dictionary_from_list(generated_list_of_dict))

if __name__ == '__main__':
    run()