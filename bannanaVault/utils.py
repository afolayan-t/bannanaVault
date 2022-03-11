import random
from string import ascii_uppercase, digits, punctuation

def replace(char):
    return (
        random.choice([char.capitalize(), random.choice(punctuation + digits)])
        if random.choice([True, False])
        else char
   )
