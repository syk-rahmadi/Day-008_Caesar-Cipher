

def prime_checker(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2): # Check for factors up to the square root of the number
            if number % i == 0:
                return False
        return True

# Example usage
number = int(input("Give your number? "))
if prime_checker(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")



