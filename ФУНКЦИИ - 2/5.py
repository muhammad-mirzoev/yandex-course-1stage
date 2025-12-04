l1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
      'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
      'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', '']
l2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
      'eighty', 'ninety']


def number_in_english(number):
    if not number:
        return 'zero'
    if number // 100 and number % 100:
        result = '{} hundred and '.format(l1[number // 100 - 1])
    elif number // 100:
        result = '{} hundred'.format(l1[number // 100 - 1])
    else:
        result = ''
    if number % 100 <= 19:
        result += l1[number % 100 - 1]
    else:
        result = result + l2[number % 100 // 10 - 2] + ' ' + l1[number % 10 - 1]
    return result


print(number_in_english(21))