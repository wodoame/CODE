from loops import String
from random import randint
from time import sleep
from threading import Thread


def readFrom(filename: str, hashmap: dict)->None:
    with open(filename, "r") as file:
        container = file.readlines()  # a list of all lines
        char = "\\n"
        for line in container:
            dot = line.index(".")
            key = int(line[0:dot])
            value = line[dot + 1:-1]
            if char in value:
                spacing = ' '* len(f"question_____")
                strings = value.split(char)
                value = f"\n{spacing}".join(strings)
            hashmap.update({key: value})


def timer():
    """timing function"""
    global time_limit
    time_limit = 30
    for i in range(time_limit):
        time_limit -= 1
        sleep(1)

    print("[time is up!!; enter final answer]", end=" >> ")








def set_timer():
    time_limiter = Thread(target=timer)
    time_limiter.start()

def main():
    """main function"""
    filename_q = "C:\\Users\\WODOAME\\Desktop\\new_repository\\sample.txt"
    filename_a = "C:\\Users\\WODOAME\\Desktop\\new_repository\\answers.txt"

    questions = {}
    answers = {}
    readFrom(filename_q, questions)
    readFrom(filename_a, answers)

    def main_logic(score):


        j = randint(1, len(questions))
        k = 1
        set_timer()
        score = score 
        while time_limit > 0:
            answer = input(f"\nquestion {k}: {questions.get(j)} >> ").lower().strip()
            if answer == answers.get(j):
                print("[that's correct]")
                score += 5
            else:
                print("[that's incorrect]")
            j = randint(1, len(questions))
            k += 1

        print("\nyour score = {}".format(score))
    
        command = String.loopIfElse("\ndo you want to retry(y/n) >> ", "y", "n", messageIfError="[wrong-input]; only 'y' or 'n' accepted")
        
        if command == "y":
            main_logic(0)


    main_logic(0)            





if __name__ == "__main__":
    main()


