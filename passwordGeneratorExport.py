import random
from loops import Int, String
import string


def main():
    def algorithms(): 
        n = Int.checkValueError("\nhow many characters are in the password >> ")
        sample = Int.checkValueError("how many samples >> ")
        
        print()
        stringLower = string.ascii_lowercase 
        stringUpper = string.ascii_uppercase
        numbers = string.digits
        specialCharacters = string.punctuation 
        elements = [stringLower, stringUpper, numbers, specialCharacters]

        for sample_range in range(sample):
            result = ""
            for iterable in elements:
                result += random.choice(iterable)
            r = n - 4
            combination = "".join(elements)
            result += "".join(random.choices(combination, k=r))
            print(f"generated password >> {''.join(result)}")


    
        
        command = String.loopIfElse("\ndo you want to continue >> ", "y", "n")

        if command == "y":
            algorithms()
    
    
    
    
    algorithms()








if __name__ == "__main__":
    main()
