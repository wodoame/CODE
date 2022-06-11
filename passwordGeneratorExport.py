def main():
    import random
    from loops import Int, String
    
    
    def algorithms(): 
        n = Int.checkValueError("\nhow many characters are in the password >> ")
        sample = Int.checkValueError("how many samples >> ")
        
        print()
        stringLower = "abcdefghijklmnopqrstuvwxyz"
        stringUpper = stringLower.upper()
        numbers = "1234567890"
        specialCharacters = "@.-&"
        elements = [stringLower, stringUpper, numbers, specialCharacters]

        for sample_range in range(sample):
            result = []
            for item in elements:
                result += random.choices(item, k=1)
            r = n - 4
            combination = "".join(elements)
            result += random.choices(combination, k=r)
            print(f"generated password >> {''.join(result)}")


    
        
        command = String.loopIfElse("\ndo you want to continue >> ", "y", "n")

        if command == "y":
            algorithms()
    
    
    
    
    algorithms()








if __name__ == "__main__":
    main()
