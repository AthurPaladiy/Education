# 4th program
n1 = 13.42
n2 = 42.13


def npi(x):
    return int(x)


def npf(x):
    return int(x * 100 % 100)


print(npi(n1) == npf(n2) or npi(n2) == npf(n1))
