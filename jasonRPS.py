from random import randint
from loops import String, Int

def main()->None:
    s_dict = {
        1: "rock",
        2: "paper",
        3: "scissors"
              }

    com = randint(1, 3)
    user = Int.checkValueError("1 ~ rock\n2 ~ paper\n3 ~ scissors\ninput = ", "strings and floats not allowed\n")
    print(f"computer = {s_dict.get(com)}; user = {s_dict.get(user, 'invalid-input')}")
    if user == com:
        print("it was a tie")
    elif user == 1 and com == 3: 
        print("you win")
    elif user == 1:
        print("computer won")
    elif user == 2 and com == 1:
        print("you win")
    elif user == 2:
         print("computer won")
    elif user == 3 and com == 2:
        print("you win")
    elif user == 3:
        print("computer won")

    command = String.loopIfElse("do you want to retry the game(y/n) >> ", "y", "n", messageIfError="[wrong-input]; only 'y' or 'n' accepted\n")
    if command == "y":
        print()
        main()

if __name__ == "__main__":
    main()
