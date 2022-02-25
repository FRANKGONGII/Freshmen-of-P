def break_words(stuff):
    """
    this function will break words for us
    :param stuff:
    :return:
    """
    words = stuff.split(' ')
    return words


def sort_words(words):
    """
    sort the words
    :param words:
    :return:
    """
    return sorted(words)


def print_first_word(words):
    """
    Printfs the first word after popping it off
    :param words:
    :return:
    """
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """
    print the last word after popping it off
    :param words: 
    :return: 
    """
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """
    Takes in a full sentence and returns the sorted words
    :param sentence:
    :return:
    """
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """
    prints the first and last words in the sentence
    :param sentence:
    :return:
    """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """
    sorts the words then prints the first and last words
    :param sentence:
    :return:
    """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
