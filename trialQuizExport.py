def main():
    """main function"""
    from random import randint
    from time import sleep
    from threading import Thread

    def timer():
        """timing function"""
        global time_limit
        time_limit = 30
        for i in range(time_limit):
            time_limit -= 1
            sleep(1)
        print("\ntime is up!!\nenter your final answer")


    def set_timer():
        time_limiter = Thread(target=timer)
        time_limiter.start()

    questions = {
                
        1: "given two vectors a and b, what is the name for a x b or b x a ? >> ",
        2: "i and k are standard basis vectors, i x k >> ",
        3: "the sum of all entries in the main diagonal of a matrix is called what? >> ",
        4: "how many ways can you arrange 5 distinct items in a single line? >> ",
        5: "what is the name of the invisible force that pulls objects to the surface of the earth >> ",
        6: "I am the field of mathematics that studies the likelihood of an event happening >> ",
        7: "the difference between the maximum and minimum value of sin(x), where x is an angle, is: >> ",
        8: "i and j are standard basis vectors i x j = >> ",
        9: "provided n is an integer, if n mod 2 == 0 then n has to be even\nTrue or False >> ",
        10: "what is the value of e^(ln(3.142)) >> "

    }
    answers = {
        
        1: "cross product",
        2: "-j",
        3: "trace",
        4: "120",
        5: "gravity",
        6: "probability",
        7: "2",
        8: "k",
        9: "true",
        10: "3.142"
    }

    j = randint(1, len(questions))
    k = 1
    score = 0
    set_timer()
    do_loop = True
    while do_loop:
        while time_limit > 0:
            answer = input(f"\nquestion {k}: {questions.get(j)}").lower().strip()

            if answer == answers.get(j, "\nnone"):
                print("that's correct")
                score += 5
            else:
                print("that's incorrect")
            j = randint(1, len(questions))
            k += 1
        print("\nyour score = {}".format(score))
       
        input_1 = False
        while not input_1:
            command = str(input("\ndo you want to retry(y/n): ")).strip()
            if command == "y":
                j = randint(1, len(questions))
                k = 1
                score = 0
                set_timer()
                break
            elif command == "n":
                do_loop = False
                break
            else:
                print("\n[wrong-input]; only 'y' or 'n' accepted")





if __name__ == "__main__":
    main()
    
