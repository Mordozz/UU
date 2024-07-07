numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_prime = []

for i in numbers:
    if i < 2:
        continue
    is_prime = True
    for j in range(2, i):
        if j * j > i:
            break
        if i % j == 0:
            is_prime = False
            not_prime.append(i)
            break
    if is_prime:
        primes.append(i)

print(f"{'Простые числа'.center(20,'*')}\n", primes)
print(f"{'Неростые числа'.center(20,'*')}\n", not_prime)
