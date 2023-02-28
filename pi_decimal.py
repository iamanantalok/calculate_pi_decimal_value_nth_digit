
# Find PI to the Nth Digit
# Have the user enter a number 'n'
# and print out PI to th 'n'th digit

def calPi(limit):
    '''
    Print out the digits of PI until it reaches the given limit
    :param:  limit
    :return: Pi decimal
    '''

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            # yeild digit
            yield n
            # insert period after first digit
            if counter == 0:
                yield '.'
            # end
            if decimal == counter:
                print('')
                break
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr


def main():

    # calls calPi with given limit
    pi_digits = calPi(int(input("Enter number of decimals to calculate to")))

    i = 0

    # Print the output of calPi generator function
    # insert a newline after every 20th number

    for d in pi_digits:
        print(d,end='')
        i += 1
        if i == 20:
            print("")
            i= 0

if __name__ == '__main__':
    main()