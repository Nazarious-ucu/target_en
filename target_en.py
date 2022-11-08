from typing import List
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    grid_result = []
    letter_list = list(map(chr, range(ord('A'), ord('Z') + 1)))
    for i in range(3):
        help_list = []
        for k in range(3):
            help_list.append(random.choice(letter_list))
        grid_result.append(help_list)
    return grid_result


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f, 'r') as file:
        result_word_list = []
        for one_letter in letters:
            for line in file:
                if ord(line[:1]) < ord(one_letter):
                    continue
                line = line[:-1]
                lst_of_letters = list(letters)
                if_in_letters = False
                if line[:1] == one_letter:
                    for i in line:
                        if i in lst_of_letters:
                            lst_of_letters.remove(i)
                            if_in_letters = True
                        else:
                            if_in_letters = False
                            break
                    if if_in_letters:
                        result_word_list.append(line)
                if line[:1] == chr(ord(one_letter) + 1):
                    file.seek(0)
                    break
        return result_word_list

# print(get_words('C:/Users/1/Nazar_work/target_en/en.txt', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    result_user_list = []
    print("Inpur words")
    while True:
        try:
            result_user_list.append(input())
        except EOFError:
            break
    return result_user_list

# print(get_user_words())

def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
