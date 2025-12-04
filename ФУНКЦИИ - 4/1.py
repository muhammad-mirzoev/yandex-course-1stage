def parrot(phrase):
    if not hasattr(parrot, 'heard_phrases'):
        parrot.heard_phrases = set()

    if phrase in parrot.heard_phrases:
        print(phrase)
    else:
        parrot.heard_phrases.add(phrase)


parrot("Привет")
parrot("Как тебя зовут?")
parrot("Привет")