numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = False
    division_wr_counters = 0
    for k in numbers:
        division = i % k
        if division == 0:
            division_wr_counters += 1
        elif division_wr_counters == 2:
            is_prime = True
            continue
        elif division_wr_counters == 3:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    elif i > 1:
        not_primes.append(i)
print('Primes:', primes)
print('Not Primes:', not_primes)
