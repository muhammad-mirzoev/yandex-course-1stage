input_string = input()

has_liliput = ('лилипут' in input_string or 'Лилипут' in input_string or 'ЛИЛИПУТ' in input_string)
has_velikan = ('великан' in input_string or 'Великан' in input_string or 'ВЕЛИКАН' in input_string)

if has_liliput and has_velikan:
    print("Я совсем запутался.")
elif has_liliput:
    print("В Лилипутии.")
elif has_velikan:
    print("В Великании.")
else:
    print("Я совсем запутался.")