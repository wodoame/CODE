def main():
    # solving a system of three equations using the Gauss elimination method
    # The equations are of the form ax + by + cz = d
    
    n = "no-value-input"
    while n == "y" or n == "no-value-input":
        try:
            R1, R2, R3, = [], [], []
            print("\n[enter the first row]\n")
            for i, element in enumerate(range(4)):
                R1.append(float(input("a1{} = ".format(i + 1))))
            print("\n[enter the second row]\n")
            for i, element in enumerate(range(4)):
                R2.append(float(input("a2{} = ".format(i + 1))))
            print("\n[enter the third row]\n")
            for i, element in enumerate(range(4)):
                R3.append(float(input("a3{} = ".format(i + 1))))
            print("\n[augmented matrix form]\n{}\n{}\n{}\n".format(R1, R2, R3))
            if R1[0] == 0 and R2[0] != 0:
                R1, R2 = R2, R1
            elif R1[0] == 0 and R3[0] != 0:
                R1, R3 = R3, R1



            if R1[0] != 0:
                R1 = list(map(lambda x: x / R1[0], R1))
                if R2[1] - R1[1] * R2[0] == 0:
                    R2, R3 = R3, R2

                R2 = list(map(lambda x, y: (x - y*R2[0]), R2, R1))
                R2 = list(map(lambda x: x/R2[1], R2))
                R3 = list(map(lambda x, y: (x - y*R3[0]), R3, R1))
                R3 = list(map(lambda x, y: (x - y*R3[1]), R3, R2))
                R3 = list(map(lambda x: x/R3[2], R3))
                # for more simple answers let:
                R2 = list(map(lambda x, y: x - y*R2[2], R2, R3))
                z1 = R3[3]
                y1 = R2[3]
                x1 = R1[3]-(R1[1]*y1 + R1[2]*z1)
                print("x = {}; y = {}; z = {}".format(x1, y1, z1))
  
                print("[rounded 1 dp]\nx = {}; y = {}; z = {}\n".format(round(x1, 1), round(y1, 1), round(z1, 1)))
                
                print("[rounded 2 dp]\nx = {}; y = {}; z = {}\n".format(round(x1, 2), round(y1, 2), round(z1, 2)))
                
                print("[rounded 3 dp; student-suitable]\nx = {}; y = {}; z = {}\n".format(round(x1, 3), round(y1, 3), round(z1, 3)))
        except ZeroDivisionError:
            print("[can't solve]\n")
        except ValueError:
            print("[no entry recorded the entry]\n")
        finally:
            inputType = "none-yet"
            while inputType == "not-correct" or inputType == "none-yet":
                n = str(input(">> do you want to retry(y/n) input = ").lower().strip())
                if n == "y" or n == "n":
                    break
                elif n != "n" or n != "y":
                    inputType = "not-correct"
                    print("[wrong input]\n")


if __name__ == "__main__":
    main()
