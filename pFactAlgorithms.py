from collections import Counter
import time
def factorize(n, array, primes_list):
    completed = False
    result = n
    i = 0
    while result != 1:
        if result % array[i] == 0:
            result = int(result/ array[i])
            primes_list.append(array[i])
        else:
            i += 1
            completed = True

        if i == len(array) and result != 1:
            completed = False
            break
    return [result, primes_list, completed]

def show(element, n):
    string = ""
    for i, j in element.items():
        string += f"({i} ^ {j}) x " if j != 1 else f"{i} x "
    return f"prime factorization of {n} = {string[0:len(string) - 2]}"

def main():

    # prime factorization
    # all prime numbers apart from 2 and 3 satisfy 6n + 1 and 6n - 1, n is an integer
    # except the multiples of primes . that is they also satisfy this formula
    # also f(n) = n ^ 2 + n + 41 where f(n) is a prime and and n is from 0 to 39 this ; note that f(n) can only be greater than 40
    # the limitation with this formula is that not all primes above 40 are generated
    # in short there is no such formula that generates all primes without exceptions
    # even numbers apart from 2 are not prime
    # primes are odd integers
    # if the sum of digits of a number is divisible by 3 then it is not prime

    start_time = time.time()
    basic_primes = [2, 3, 5, 7, 11, 13, 17, 19]
    n = int(input("enter an integer >> "))

    output = factorize(n, basic_primes, [])

    if not output[2]:
        ints = (i for i in range(23, n + 1, 2) if n % i == 0 and (int(i + 1) % 6 == 0 or int(i-1) % 6 == 0))
        # list of elements that will contain a prime and may or may not contain some other numbers that are not primes.
        ints = list(ints)
        final = factorize(output[0], ints, output[1])
        display = Counter(final[1])
        print(show(display, n))
    else:
        display = Counter(output[1])
        print(show(display, n))


    end_time = time.time()
    print(f"\nt = {end_time - start_time} ms")



if __name__ == "__main__":
    main()
