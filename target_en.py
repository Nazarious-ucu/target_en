from typing import List
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    pass


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    pass

# print(get_words('C:/Users/1/Nazar_work/target_en/en.txt', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    pass

def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    result_pure_list = list(user_words)
    for word in user_words:
        if word in words_from_dict or not letters[4] in word:
            result_pure_list.remove(word)
            continue
        help_letters = list(letters)
        for letter_word in word:
            if not letter_word in help_letters:
                result_pure_list.remove(word)
                continue
            else:
                help_letters.remove(letter_word)
    return result_pure_list


# print(get_pure_user_words())
def results():
    file_str = ''
    letters = generate_grid()
    # letters = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'K']]
    letters_lst = [j.lower() for i in letters for j in i]
    letters_str = ''.join(letters_lst)
    print('Your list of letter:' + letters_str)
    file_str += 'Your list of letter:' + letters_str + '\n'

    user_words = get_user_words()
    dict_words = get_words('en.txt', letters_lst)
    print('So your win words:')
    file_str += 'So your win words:\n' 
    for i in user_words:
        if i in dict_words:
            print(i, end= ' ')
            file_str += i + ' '
    file_str += '\n'

    rools_words = get_pure_user_words(user_words, letters_lst, dict_words)
    print('And your words with the rules and returns list of those words that are not in dictionary.')
    file_str += 'And your words with the rules and returns list of those words that are not in dictionary.\n'
    for i in rools_words:
        print(i, end= ' ')
        file_str += i + ' '

    with open('results.txt', 'w') as file:
        file.write(file_str)

    


