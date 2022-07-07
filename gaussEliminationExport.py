from loops import Float, String


def main():
    # solving a system of three equations using the Gauss elimination method
    # The equations are of the form ax + by + cz = d
    def algorithms():

        try:
            R1, R2, R3, = [], [], []
            print("\n[enter the first row]")
            for i, element in enumerate(range(4)):
                R1.append(Float.check_value_error("a1{} = ".format(i + 1)))
            print("\n[enter the second row]")
            for i, element in enumerate(range(4)):
                R2.append(Float.check_value_error("a2{} = ".format(i + 1)))
            print("\n[enter the third row]")
            for i, element in enumerate(range(4)):
                R3.append(Float.check_value_error("a3{} = ".format(i + 1)))

            if R1[0] == 0 and R2[0] != 0:
                R1, R2 = R2, R1
            elif R1[0] == 0 and R3[0] != 0:
                R1, R3 = R3, R1

            # main row operations
            if R1[0] != 0:
                R1 = list(map(lambda x: x / R1[0], R1))
                if R2[1] - R1[1] * R2[0] == 0:
                    R2, R3 = R3, R2

                R2 = list(map(lambda x, y: (x - y * R2[0]), R2, R1))
                R2 = list(map(lambda x: x / R2[1], R2))
                R3 = list(map(lambda x, y: (x - y * R3[0]), R3, R1))
                R3 = list(map(lambda x, y: (x - y * R3[1]), R3, R2))
                R3 = list(map(lambda x: x / R3[2], R3))
                R2 = list(map(lambda x, y: x - y * R2[2], R2, R3))
                z1 = R3[3]
                y1 = R2[3]
                x1 = R1[3] - (R1[1] * y1 + R1[2] * z1)
                print("\nx = {}; y = {}; z = {}".format(x1, y1, z1))
                print("\n[rounded 1 dp]\nx = {}; y = {}; z = {}".format(round(x1, 1), round(y1, 1), round(z1, 1)))
                print("\n[rounded 2 dp]\nx = {}; y = {}; z = {}".format(round(x1, 2), round(y1, 2), round(z1, 2)))
                print("\n[rounded 3 dp; student-suitable]\nx = {}; y = {}; z = {}".format(round(x1, 3), round(y1, 3),
                                                                                          round(z1, 3)))

        except ZeroDivisionError:
            print("\n[can't solve]")

        command = String.repeat("\ndo you want to retry(y/n) >> ", "y", "n")
        if command == "y":
            algorithms()

    algorithms()


if __name__ == "__main__":
    main()

      
