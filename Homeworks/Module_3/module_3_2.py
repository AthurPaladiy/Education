def approved(recipient, sender):
    email_mark = '@'
    approved_domains = ['.com', '.ru', '.net']
    correct_domains_recipient = False
    correct_domains_sender = False
    approve = False
    if email_mark in recipient and email_mark in sender:
        for i in range(len(approved_domains)):
            if recipient.endswith(approved_domains[i]):
                correct_domains_recipient = True
                break
        for i in range(len(approved_domains)):
            if sender.endswith(approved_domains[i]):
                correct_domains_sender = True
                break
        if correct_domains_recipient and correct_domains_sender:
            approve = True
    return approve


def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if approved(recipient, sender):
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
