def print_only_new(message):
    if not hasattr(print_only_new, 'received_messages'):
        print_only_new.received_messages = set()

    if message not in print_only_new.received_messages:
        print(message)
        print_only_new.received_messages.add(message)


print_only_new('Шутка номер 15')
print_only_new('Шутка номер 23')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 100')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 99')
print_only_new('Шутка номер 15')
print_only_new('Шутка номер 100')