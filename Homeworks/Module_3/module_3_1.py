calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    info = (len(string), str.upper(string), str.lower(string))
    count_calls()
    return info


def is_contains(string, list_to_search):
    count_calls()
    info = False
    for i in range(len(list_to_search)):
        if str.lower(string) == str.lower(list_to_search[i]):
            info = True
    return info


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
