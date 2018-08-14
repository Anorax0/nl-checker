from text_character_checker.functions import *
from nltk import sent_tokenize
from time import time

chosen_text = None
opt = None

if not chosen_text:
    try:
        with open(str(search_for_text()), 'r', encoding='UTF-8') as file:
            f = file.read()
            file_text = f.split()
            text = sent_tokenize(f)
    except FileNotFoundError:
        exit(f'File not found. Program closed')

    while opt != 'exit':
        opt = input(f"""\nAvailable options for text processing [{file.name}]:
                        A: Display the text.
                        B: Display the character of the text (positive/negative/neutral).
                        C: Display unclassified words.
                        D: Add a word to the lexicon.
                        E: Check the character of the word.
                        What would you like to do? \n
                        Type <exit> to close the program""")
        print('\n')
        opt = opt.lower()

        # Displays text with original formatting
        if opt == 'a':
            time_start = time()
            show_text(f)
            print(f'\nExecuting time: {time() - time_start:.6f}')
            opt = input('Would you like to display the text divided into sentences? [T/N]')
            opt = opt.lower()
            if opt == 't':
                time_start = time()
                show_sent(text)
                print(f'\nExecuting time: {time() - time_start:.6f}')
                continue

        # Shows character of the text and shows percentage of positive and negatives words
        # Shows ten first positive and negative words
        # Shows ten first unclassified words
        # Shows percentage of positive and negative words in text
        elif opt == 'b':
            time_start = time()
            print(f'Positive words:: {", ".join(check_words_character("positives", file_text))}')
            print(f'Negative words: {", ".join(check_words_character("negatives", file_text))}')
            print(f'There are {count_nochar(file_text, 10)} unclassified words.')
            z = count_words(file_text)
            x = (count_char_words('positives', file_text) / z) * 100
            y = (count_char_words('negatives', file_text) / z) * 100
            print(f'Positive words: {round(x, 2)}% of the text; negative words: {round(y,2)}% of the text.')
            print(f'\nExecuting time: {time() - time_start:.6f}')

        # Shows unclassified words
        elif opt == 'c':
            time_start = time()
            print(f'There are {count_nochar(file_text, 30)} unclassified words.')
            print(f'\nExecuting time: {time() - time_start:.6f}')

        # Adding word to suitable lexicon
        elif opt == 'd':
            word_check = input('Which word would you like to add? \n')
            if check_char(word_check) == 'null':
                add_char = input(
                    f'What character does a word <{word_check}> have?\nPositive? [input positive]'
                    f'\nNegative? [input negative]\nNeutral? [input neutral')
                time_start = time()
                print(adding(word_check, add_char))
                print(f'\nExecuting time: {time() - time_start:.6f}')
            else:
                print('The word is already in the lexicon.')

        # Checks character of the word if it is in lexicon
        elif opt == 'e':
            word = input('Write a word which you want to check:')
            time_start = time()
            print(show_char(str(word)))
            print(f'\nExecuting time: {time() - time_start:.6f}')
        # Stops the program
        elif opt == 'exit':
            print('Program closed.')


else:
    exit('Unexpected problem while opening text file.')