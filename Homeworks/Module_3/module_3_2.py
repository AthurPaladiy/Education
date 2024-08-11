def approved(recipient, sender):
    # Определяем символ '@' как признак email-адреса
    email_mark = '@'

    # Список допустимых доменов
    approved_domains = ['.com', '.ru', '.net']

    # Переменные для отслеживания корректности доменов у получателя и отправителя
    correct_domains_recipient = False
    correct_domains_sender = False

    # Переменная, которая будет возвращать результат функции
    approve = False

    # Проверяем, содержат ли оба адреса символ '@'
    if email_mark in recipient and email_mark in sender:

        # Проверка домена у получателя
        for i in range(len(approved_domains)):
            if recipient.endswith(approved_domains[i]):
                correct_domains_recipient = True
                break

        # Проверка домена у отправителя
        for i in range(len(approved_domains)):
            if sender.endswith(approved_domains[i]):
                correct_domains_sender = True
                break

        # Устанавливаем approve в True, если домены корректны у обоих
        if correct_domains_recipient and correct_domains_sender:
            approve = True

    # Возвращаем результат проверки
    return approve


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    # Проверяем, одобрены ли адреса получателя и отправителя
    if approved(recipient, sender):

        # Проверка, не отправляется ли письмо самому себе
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')

        # Если отправитель по умолчанию (университетский адрес)
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

        # Если отправитель отличается от стандартного
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

    # В случае если домены не одобрены
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


# Тестовые вызовы функции send_email

# Отправляем письмо с университетского адреса на корректный адрес
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

# Отправляем письмо с нестандартного отправителя на корректный адрес
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

# Отправляем письмо с некорректным доменом отправителя
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

# Пытаемся отправить письмо самому себе
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
