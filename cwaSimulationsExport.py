from loops import Int, Float, String

def main(): 
    
    # cwa calculations  # prev_num = previous numerator ; prev_den = previous denominator ; array stores cwas
    
    
    def main_logic(prev_num, prev_den, array): # parameters are initial conditions  
        total_credits = 0 
        points_obtained = 0 # always starts at zero per semester  
        total_points = 0   
        course_count = Int.check_value_error("\nenter the number of courses >> ")

        for i in range(course_count):
            score = Float.check_value_error(f"\ncourse[{i + 1}]\nscore >> ")
            credit = Int.check_value_error("credit hour(s) >> ")
            
            points_obtained += (score * credit)
            total_credits += credit 
        if total_credits != 0:
            total_points = (total_credits * 100) + prev_den 
            points_obtained += prev_num 
            cwa = (points_obtained / total_points) * 100
            array.append(cwa)
            print(f"\ncwa progress = {array};\ncurrent cwa = {cwa};\nfriction = {total_points/100}")
        elif total_credits == 0:
            print("\n[can't calculate;  total credits = 0]")
        command = String.repeat("\ndo you want to continue calculating? >> ", "y", "n")
        if command == "y":
            print("\nNote: further calculations will be added to your previous results to make a new cwa")
            prev_num = points_obtained 
            prev_den = total_points
            main_logic(prev_num, prev_den, array)
    main_logic(0, 0, [])        
                        
        
                     
            
            
            
            

            








if __name__ == "__main__":
    main()

            




