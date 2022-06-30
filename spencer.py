def n_format(s_list: list, arg: bool = False)->str:

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    mat = s_list
    plus = "+"
    minus = "-"
    # taking each string in the list one at a time
    for element in mat:
        a_list = element.split() # splitting separates the elements and puts them in another array
        a = a_list[0] # setting a to the first number in the list
        b = a_list[2] # setting b to the second number in the list
        if plus in a_list:
            sep = plus
            result = int(a) + int(b)
        else:
            sep = minus
            result = int(a) - int(b)
        result = str(result) #
        l_result = len(result)
        maxi = len(max(a_list, key=len)) # finding the maximum item by length in the list
        if l_result >= maxi: #
            k = len(result) + 2 # the number of times the dash (-) has to be printed
            d1 = l_result - len(a) # this will define the spacing for first number
            d2 = l_result - len(b) # this will define the spacing for the second number

            line1 += f"  {' '*d1}{a}   "
            line2 += f"{sep} {' '*d2}{b}   "
            line3 += f"{'-'*k}   "
            line4 += f"  {result}   " if arg else ""
        else:
            k = maxi + 2
            d1 = maxi - len(a) # defines the spacing for the first number
            d2 = maxi - len(b) # defines the spacing for the second number
            d3 = maxi - l_result # defines the spacing for the result

            line1 += f"  {' '*d1}{a}   "
            line2 += f"{sep} {' '*d2}{b}   "
            line3 += f"{'-'*k}   "
            line4 += f"  {' '*d3}{result}   " if arg else ""


    return f"{line1}\n{line2}\n{line3}\n{line4}"
