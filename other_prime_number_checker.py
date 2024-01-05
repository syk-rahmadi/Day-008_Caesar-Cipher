#Other prime checker function


def primeCheck (number):
    if_prime = True
    for i in range (2, number):
        if number % i == 0:
            if_prime = False
    if if_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

number = int(input("Give your choosen number?"))
primeCheck(number)