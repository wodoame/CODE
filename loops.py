class Int:
    @staticmethod
    def checkValueError(message, messageIfError=""):
        while True:
            try: 
                input_val = int(input(message))
            except ValueError: 
                print(messageIfError)
            else: 
                return input_val
    

    




class String:
    @staticmethod
    def loopIfElse(message, *values, messageIfError=""): 
        while True: 
            input_val = str(input(message)).lower().strip()
            if input_val not in values: 
                print(messageIfError)
            else: 
                return input_val 

           
        



class Float:
    @staticmethod
    def checkValueError(message, messageIfError=""): 
        while True:
            try: 
                input_val = float(input(message))
            except ValueError: 
                print(messageIfError)
            else: 
                return input_val
    

    




















