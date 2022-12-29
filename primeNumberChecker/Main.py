def prime_checker(number):
    prime = True
    if number in [0,1]:
        prime = False
    elif number > 2:
        for divisor in range (2, number):
            if number%divisor == 0:
                prime = False
                break

    if prime:
        print('Prime Number!!')
    else:
        print('Not a Prime Number!!')

n = int(input('Check this number : '))
prime_checker(number=n)