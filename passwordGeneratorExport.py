def main():
    import random
    input_1 = False
    while not input_1:
        try:
            n = int(input("\nhow many characters are in the password >> "))
            sample = int(input("how many samples >> "))
        except ValueError:
            print("\n[wrong-input]; password and sample length can only be integers")
            continue
        else:
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

    
    
        do_loop = True
        while do_loop:
            command = str(input("\ndo you want to retry?(y/n) >> ")).lower().strip()
            if command == "y":
                break
            elif command == n:
                input_1 = True
                break
            else:
                print("\n[wrong-input]; only 'y' or 'n' accepted")








if __name__ == "__main__":
    main()