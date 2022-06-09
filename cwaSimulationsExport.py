def main(): 
    """main function"""
    # cwa calculations
    prev_denominator = 0
    prev_numerator = 0 
    cwas = []
    
      
    input_1 = False 
    while not input_1:
        total_credits = 0 
        points_obtained = 0
        total_points = 0   
        try: 
            course_count = int(input("\nenter the number of courses >> "))
        except ValueError: 
            print("\n[wrong-input]; only integers accepted")
            continue 
        else: 
            input_2 = False 
            for i in range(course_count):
                while not input_2:
                    try: 
                        score = float(input(f"\ncourse[{i + 1}]\nenter score >> "))
                        credit = int(input("enter credit hours >> "))
                    except ValueError: 
                        print("\n[wrong-input]; cannot calculate")
                        continue 
                    else: 
                        points_obtained += (score * credit)
                        total_credits += credit 
                        break 
            
            
            
            total_points = (total_credits * 100) + prev_denominator  
            points_obtained += prev_numerator 
            cwa = (points_obtained / total_points) * 100 
            cwas.append(cwa)
            print(f"\ncwa progress = {cwas};\ncurrent cwa = {cwa};\nfriction = {total_points/100}")
        
            do_loop = True 
            while do_loop:
                command = str(input("\ndo you want to continue calculating?(y/n) >> ")).lower().strip()
                if command == "y":
                    print("\nNote: further calculations will be added to your previous results to make a new cwa")
                    prev_numerator = points_obtained 
                    prev_denominator = total_points 
                    break 
                elif command == "n":
                    input_1 = True  
                    break 
                else:
                    print("\n[wrong-input]; only 'y' or 'n' accepted") 
            

            








if __name__ == "__main__":
    main()
