from os import replace
#import re                                              # uncoment if need to split by signs several 

# 1: What if appear "?" or "!" ?
# 2: What if "I" exist in the middle of sentence?
# 3: Should we remove white spaces?
# 4: After ":" should be uppercase word?
# 5: Should be replace_iz_on_is(a) independent funcion? (at themoment, for result we use it with function normalize_letter_case(a))
# 6: Fix“iz” Should be here space?

def normalize_letter_cases(some_text):
    ''' Normalize input text from letter cases point of view. Sentences will be trimmed'''
    result_text = some_text.lower()
    inner_text = result_text.split('.')                         
    #inner_text = re.split('! | ? |\. ', result_text)   #if need split by ? ! . 
    normalize_text = ''

    for sentence in inner_text:
       fix_text = sentence.replace(sentence, sentence.strip().capitalize())
       if fix_text != "":                              # we don't include last element([]) after split() 
           normalize_text = normalize_text + fix_text + '. '
    normalize_text = normalize_text [:-1]              # delele space in the end
    
    return normalize_text

# # Alternative way for normalize_letter_cases(a)

# def normalize_letter_cases(some_text):
#     ''' Normalize input text from letter cases point of view. Sentences will be trimmed'''

#     result_text = some_text.lower()
#     inner_text = result_text.split('.')                         
#     normalize_text = ''

#     key = 0                             # index of empty list element
#     for sentence in inner_text:
#         if(sentence == ''):             #if we have empty list element
#             inner_text.pop(key)
#             key = key + 1
#             continue
#         key = key + 1

#         k=0
#         while sentence[k].isspace():       
#             k = k + 1                     # find first letter in sentence
#         fix_text = sentence[:k] + sentence[k].capitalize() + sentence[k+1:]

#         #if fix_text != "":                              
#         normalize_text = normalize_text + fix_text + '. '
#     normalize_text = normalize_text [:-1]
    
#     return normalize_text



def sentence_with_last_words(some_text):
    ''' Create sentence with last words of each existing sentence in input text '''
    inner_text = some_text.split('.')
    res = ''
    for sentence in inner_text:    
        if sentence != "":   
            res = res + sentence.split()[-1] + ' '
    res = res[:-1]
    res = res + '.'

    return res

def replace_iz_on_is(some_text):
    '''Replace "iz on "is" '''

    result = some_text.replace('iz ','is ')
   
    return result

def number_of_spaces(some_text):
    '''Count number of spase and whitespace. Return their total number.'''
    numb_sp = some_text.count(' ')
    numb_white_sp = some_text.count('\n')
    sum = numb_sp + numb_white_sp
    print('numb_white_sp: ',numb_white_sp)           
    print('numb_sp: ',numb_sp)
    return sum


def run():
    ''' The main function'''

    text = open("README.txt", "r").read()        # Get text from file
    answer = normalize_letter_cases(text)
    print(answer, '\n')
    print ('With last wodrs:', answer + ' ' + sentence_with_last_words(answer).capitalize(), '\n')
    print('Replace iz on is:', replace_iz_on_is(answer) , '\n' )
    print('Number of spaces:', number_of_spaces(text))



if __name__ == '__main__':
    run()