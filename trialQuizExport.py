from loops import String
from random import randint
from time import sleep
from threading import Thread


def read_from(filename: str, hashmap: dict) -> None:
    with open(filename, "r") as file:
        container = file.readlines()
        char = "\\n"
        for line in container:
            line = line.rstrip()
            dot = line.index(".")
            key = int(line[0:dot])
            value = line[dot + 1:]
            if char in value:
                spacing = f"\t\t\t  "
                strings = value.split(char)
                value = f"\n{spacing}".join(strings)
            hashmap.update({key: value})


def timer() -> None:
    """timing function"""
    global time_limit
    time_limit = 20
    for i in range(time_limit):
        time_limit -= 1
        sleep(1)

    print("[time is up!!; enter final answer]", end=" >> ")


def set_timer() -> None:
    time_limiter = Thread(target=timer)
    time_limiter.start()


def main() -> None:

    filename_q = "C:\\Users\\WODOAME\\Desktop\\DC_MACHINES\\questions.txt"
    filename_a = "C:\\Users\\WODOAME\\Desktop\\DC_MACHINES\\answers.txt"

    questions = {}
    answers = {}
    read_from(filename_q, questions)
    read_from(filename_a, answers)

    def main_logic(score) -> None:

        j = randint(1, len(questions))
        k = 1
        set_timer()
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

        command = String.repeat("\ndo you want to retry(y/n) >> ", "y", "n", error_message="[wrong-input]; only 'y' or 'n' accepted")

        if command == "y":
            main_logic(0)

    main_logic(0)


if __name__ == "__main__":
    main()
    

