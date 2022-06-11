class Int: 
    def checkValueError(message, messageIfError=""):
        check = True 
        while check:
            try: 
                input_val = int(input(message))
            except ValueError: 
                print(messageIfError)
            else: 
                return input_val
   




class String: 
    def loopIfElse(message, *values, messageIfError= ""):
        check = True 
        while check: 
            input_val = str(input(message)).lower().strip()
            if input_val not in values: 
                print(messageIfError)
            else: 
                return input_val 

  


class Float:
    def checkValueError(message, messageIfError=""):
        check = True 
        while check:
            try: 
                input_val = float(input(message))
            except ValueError: 
                print(messageIfError)
            else: 
                return input_val
    






