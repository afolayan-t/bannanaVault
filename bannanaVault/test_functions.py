import math
import random 
from string import ascii_letters

punctuation = r"""!"#$%&'()*+,-./:;=?@[]^_`{|}~"""

def generate_password():
        """Called in save function, to generate password for user."""
        password = "".join(random.choice(ascii_letters) for _ in range(10))   
        index = random.randint(0,9)
        password = password[:index] + "".join(random.sample(punctuation, 2)) + password[index+2:]
        return password

if __name__ == "__main__":
    print(generate_password())