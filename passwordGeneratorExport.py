import random
from loops import Int, String
import string


def main():
    def algorithms():
        n = Int.check_value_error("\nhow many characters are in the password >> ", error_message="[wrong-input]")
        sample = Int.check_value_error("how many samples >> ", error_message="[wrong-input]")

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

        command = String.repeat("\ndo you want to continue(y/n)>> ", "y", "n", error_message="[wrong-input]")

        if command == "y":
            algorithms()

    algorithms()


if __name__ == "__main__":
    main()
