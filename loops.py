class Int:
    @staticmethod
    def check_value_error(message, error_message=""):
        while True:
            try:
                input_val = int(input(message))
            except ValueError:
                print(error_message)
            else:
                return input_val


class String:
    @staticmethod
    def repeat(message, *values, error_message=""):
        while True:
            input_val = str(input(message)).lower().strip()
            if input_val not in values:
                print(error_message)
            else:
                return input_val


class Float:
    @staticmethod
    def check_value_error(message, error_message=""):
        while True:
            try:
                input_val = float(input(message))
            except ValueError:
                print(error_message)
            else:
                return input_val

    




















