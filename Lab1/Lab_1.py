from math import sqrt


def first_function(number):
    if type(number) is int:
        if number % 2 == 0:
            return True
        else:
            return False
    else:
        return ""


def second_function():
    prime_numbers = []
    num = 1
    while len(prime_numbers) < 5:
        if num > 1:
            prime_flag = True
            for i in range(2, int(sqrt(num)) + 1):
                if num % i == 0:
                    prime_flag = False
                    break
            if prime_flag:
                prime_numbers.append(num)
        num += 1
    return sum(prime_numbers)


def third_function(n: int):
    if n <= 1:
        return 1
    return int("1" * n) + third_function(n-1)


print(first_function(''))
print(first_function(16))
print(first_function(9))

print(second_function())

print(third_function(2))
print(third_function(5))
print(third_function(9))
