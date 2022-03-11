import math
import secrets
import random 
from string import ascii_letters, digits, punctuation, ascii_uppercase

punctuation = r"""!"#$%&'()*+,-./:;=?@[]^_`{|}~"""

def generate_password():
        """Called in save function, to generate password for user."""
        password = "".join(random.choice(ascii_letters) for _ in range(10))   
        index = random.randint(0,9)
        password = password[:index] + "".join(random.sample(punctuation, 2)) + password[index+2:]
        print(f'password generated: {password}')
        return password


def clean_new_line(string):
        # return string[:-1] if "\n" in string else string
        return string.rstrip()


def turn_to_list(filename: str):
        """excepts a text file and returns a list of the lines in that txt file"""
        with open(filename) as f:
                lines = f.readlines()
        return [ clean_new_line(i) for i in lines] 

prepositions = turn_to_list('passwords/sentences/prepositions.txt')
adjectives = turn_to_list('passwords/sentences/adjectives.txt')
nouns = turn_to_list('passwords/sentences/nouns.txt')
verbs = turn_to_list('passwords/sentences/verbs.txt')
articles = ['a', 'an', 'the']

def replace(char):
    return (
        secrets.choice([char.capitalize(), secrets.choice(punctuation + digits)])
        if secrets.choice([True, False, False])
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
    sentence = secrets.choice(articles) + secrets.choice(adjectives) + secrets.choice(nouns) + secrets.choice(prepositions) + secrets.choice(articles) + secrets.choice(adjectives) + secrets.choice(nouns)
    return "".join(replace(_) for _ in sentence)

if __name__ == "__main__":
        print(generate_password_advanced())
        
