def fractal_print(obj):
    print('[' + ', '.join(map(str, obj)) + ']')


fractal = [3]
fractal.append(fractal)
print(fractal_print(fractal))

fractal = [3]
fractal.append(fractal)
fractal.append(2)
print(fractal_print(fractal))
