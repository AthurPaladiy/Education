while 1 > 0:
    n = int(input('Введите число с первой таблички: '))
    if 2 < n < 21:
        break
    else:
        print("Посмотрите внимательней, число должно быть от 3 до 20")


def password_calc(x):
    password = []
    for i in range(1, 21):
        for k in range(1, 21):
            if i >= k:
                continue
            else:
                calc = x % (i + k)
                if calc != 0:
                    continue
                else:
                    password.extend([str(i), str(k)])
    formated_password = ''.join(password)
    return formated_password


print(password_calc(n))
