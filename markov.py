"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    line_string = ""
    open_text = open(file_path).read()
    #print(open_text)
    return open_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    list_of_words = text_string.split()
    tuple_words = tuple(list_of_words)
    for i in range(len(list_of_words) - 2):
        if (list_of_words[i], list_of_words[i+1]) in chains:
            chains[(list_of_words[i], list_of_words[i+1])].append(list_of_words[i+2])
        else:
            chains[(list_of_words[i], list_of_words[i+1])] = [list_of_words[i+2],]


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    key = choice(list(chains.keys()))
    # print(key)
    # print(type(key))

    while True:
        if(key in chains):
            random_value = choice(chains[key])
            words.append(random_value)
            key = (key[1], random_value)
            #print(key)
        else:
            break
    #print(words)

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
