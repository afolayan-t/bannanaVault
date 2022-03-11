import random
from string import ascii_uppercase, digits, punctuation
from bannanaVault.helper_functions import turn_to_list

prepositions = turn_to_list('passwords/sentences/prepositions.txt')
adjectives = turn_to_list('passwords/sentences/adjectives.txt')
nouns = turn_to_list('passwords/sentences/nouns.txt')
verbs = turn_to_list('passwords/sentences/verbs.txt')
articles = ['a', 'an', 'the']

def replace(char):
    return (
        random.choice([char.capitalize(), random.choice(punctuation + digits)])
        if random.choice([True, False])
        else char
   )

def generate_password_advanced():
    """
    Generate a sentence, and then turn into a password
    article + adjective + noun + verb + preposition + article + adjective + noun
    sentence: the brown fox jumps over the tall dog
    password: th38&0wNF0x!0mp~0v3Rt)3#@11d0G
    replacing letters with numbers and special chars at random, and removing spaces.

    pass over each letter and decide whether to ignore or replace
    if replace:
        replace with either a capitalized version, a number or a special char at random.
    """
    sentence = "".join(random.choice(articles)).join(random.choice(adjectives)).join(random.choice(nouns)).join(random.choice(verbs)).join(random.choice(articles)).join(random.choice(adjectives)).join(random.choice(nouns))
    return "".join(replace(_) for _ in sentence)
    


