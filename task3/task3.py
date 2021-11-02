def list_of_parafraphs(some_text):
    ''' Return list of paragraphs from input text.

    Divide text  into paragraphs. Capitalize first letter in paragaph.
    '''

    result_text = some_text.lower()
    inner_text = result_text.split('\n')               # Divide text by delmeter /n.
    paragraphs_list = []
    
    for paragraph in inner_text:
        fix_text = paragraph.replace(paragraph, paragraph.strip().capitalize())
        if fix_text != "":                              # We don't include last element([]) which appeared after split(). 
            paragraphs_list.append(fix_text)
    return paragraphs_list


def normalize_letter_cases(some_text):
    ''' Normalize input text from letter cases point of view.
    
    First letter in sentence rewrite uppercase. All other letter - lowercase.
    '''

    inner_text = some_text.lower().split('.') 
    fix_text = '' 
    normalize_text = ''

    for sentence in inner_text:
        fix_text = sentence.replace(sentence, sentence.strip().capitalize())
        if fix_text != "":                              
            normalize_text = normalize_text + fix_text +'. '
    normalize_text = normalize_text.replace(':.',':')          # Catch issue with ':.'
    
    return normalize_text

def replace_iz_on_is(some_text):
    '''Replace "iz on "is".'''

    addition_part = some_text.replace('Fix“iz”','Fix “iZ”')    # Catch issue with 'Fix“iZ”'. Added space and leave original 'iZ'.
    result = addition_part.replace('iz ','is ')
       
    return result

def sentence_with_last_words(some_text):
    ''' Create sentence with last words of each existing sentence in input text.'''

    inner_text = some_text.split('.')
    res = ''
    for sentence in inner_text:  
        if sentence != "" and sentence != " \n":   
            res = res + sentence.split()[-1] + ' '
    res = res[:-1]
    res = res + '.'

    return res

def catch_i(some_text):
    ''' Fix case when "I" exist not at the beginning of the sentence and it is written lowercase.'''

    some_text = some_text.replace(' i ',' I ')
    some_text = some_text.replace(' i.',' I.')
    result = some_text.replace(' i?',' I?')
    return result

def text_normalizer(some_text):
    ''' Format text in the next way:

    Return text with fixed letter cases.
    Replace "iz" on "is".
    For each paragraph add a sentence with the last words of each existing sentence in this paragraph.
    '''

    text_by_paragraphs = list_of_parafraphs(some_text)

    result = ''
    for item in text_by_paragraphs:
        norm = normalize_letter_cases(item)
        result = result + replace_iz_on_is(norm) + normalize_letter_cases(sentence_with_last_words(item)) + '\n'

    result = result.replace('Homework: Homework:','Homework:')           # 'Homework: Homework:' appeared because function list_of_parafraphs(a) divide text by delmeter /n.

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
 ''' The main function.'''
 
text = open("README.txt", "r").read()           # Get text from file.
#text = open("task3test.txt", "r").read()         # For test. 

print('Original text:', '\n',text,'\n')
print(text_normalizer(text))
print('Number of spaces:', number_of_spaces(text))


if __name__ == '__main__':
    run()