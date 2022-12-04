# A function that checks if a number is a prime number
# A prime number is a number that is only divisible by itself and 1
def check_prime_no(number):
    for i in range(2, number):
        if number % i == 0:
            return 0
    else:
        return 1


# A function that prints first 100 prime numbers
def print_100_prime_no():
    i = 1
    lists = []
    while len(lists) <= 100:
        if check_prime_no(i) == 1:
            lists.append(i)
        i += 1
    print(lists)


# call the function
print_100_prime_no()
