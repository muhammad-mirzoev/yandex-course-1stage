za = 0
protiv = 0


def voting(vote):
    global za, protiv

    if vote == "за":
        za += 1
    elif vote == "против":
        protiv += 1

    print(f"за: {za}")
    print(f"против: {protiv}")
    print()


voting("за")
voting("за")
voting("за")
voting("против")
voting("за")