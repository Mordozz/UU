def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime(func):
    def fn_wrapper(*n):
        num_sq = func(*n)
        print("Простое" if check_prime(num_sq) else "Составное")
        return num_sq

    return fn_wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)