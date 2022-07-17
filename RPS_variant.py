from random import randint
from loops import String, Int

def main() -> None:
    s_dict = {
        1: "rock",
        2: "paper",
        3: "scissors"
              }

    com = randint(1, 3)
    user = Int.check_value_error("1 ~ rock\n2 ~ paper\n3 ~ scissors\ninput = ", "strings and floats not allowed\n")
    print(f"computer = {s_dict.get(com)}; user = {s_dict.get(user, 'invalid-input')}")
    a_tuple = (user, com)
    w_message = "[you win]"
    l_message = "[computer won]"
    t_message = "[it was a tie]"
    match a_tuple:
        case (x, y) if x == y:
            print(t_message)
        case (1, 3):
            print(w_message)
        case (1, 2):
            print(l_message)
        case (2, 1):
            print(w_message)
        case (2, 3):
            print(l_message)
        case (3, 2):
            print(w_message)
        case (3, 1):
            print(l_message)

    command = String.repeat("\ndo you want to retry the game(y/n) >> ", "y", "n", error_message="[wrong-input]; only 'y' or 'n' accepted\n")
    if command == "y":
        print()
        main()

if __name__ == "__main__":
    main()
