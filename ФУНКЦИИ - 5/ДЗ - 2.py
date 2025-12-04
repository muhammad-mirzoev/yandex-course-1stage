def cleaning(*lists, **kwargs):
    result = []
    for lst in lists:
        new_lst = []
        for string in lst:
            if 'x_files' in kwargs:
                string = string.replace('X', str(kwargs['x_files']))
                string = string.replace('x', str(kwargs['x_files']))
            if 'max_len' in kwargs and len(string) > kwargs['max_len']:
                string = string[:kwargs['max_len']]
            if 'big_small' in kwargs:
                if kwargs['big_small']:
                    string = string[0].upper() + string[1:] if string else ''
                else:
                    string = string.lower()
            new_lst.append(string)
        result.append(new_lst)
    return result


data = [['Big', 'cleanups', 'are', 'fraught'],
        ['with', 'unexpected', 'finds.']]
cond = {'max_len': 6, 'big_small': True, 'x_files': 'Y'}

for item in cleaning(*data, **cond):
    print(' '.join(item))
