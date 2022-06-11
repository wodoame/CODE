def main(): 
    from loops import Int, Float, String
    # cwa calculations  #i = previous numerator ; j = previous denominator ; array stors cwas
    def main_logic(i, j, array): # parameters are initial conditions  
        total_credits = 0 
        points_obtained = 0
        total_points = 0   
        course_count = Int.checkValueError("\nenter the number of courses >> ")
        for i in range(course_count):
            score = Float.checkValueError(f"\ncourse[{i + 1}]\nscore >> ")
            credit = Int.checkValueError("credit hour(s) >> ")
            points_obtained += (score * credit)
            total_credits += credit 
        if total_credits != 0:
            total_points = (total_credits * 100) + j
            points_obtained += i
            cwa = (points_obtained / total_points) * 100
            array.append(cwa)
            print(f"\ncwa progress = {array};\ncurrent cwa = {cwa};\nfriction = {total_points/100}")
        elif total_credits == 0:
            print("\n[can't calculate;  total credits = 0]")
        command = String.loopIfElse("\ndo you want to continue calculating? >> ", "y", "n")
        if command == "y":
            print("\nNote: further calculations will be added to your previous results to make a new cwa")
            i = points_obtained 
            j = total_points 
            main_logic(i, j, array)
        
    main_logic(0, 0, [])        
                        
        
                     
            
            
            
            

            








if __name__ == "__main__":
    main()
