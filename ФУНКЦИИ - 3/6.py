friends = {}


def add_friends(name_of_person, list_of_friends):
    if name_of_person not in friends:
        friends[name_of_person] = set()
    for friend in list_of_friends:
        friends[name_of_person].add(friend)
        if friend not in friends:
            friends[friend] = set()
        friends[friend].add(name_of_person)


def are_friends(name_of_person1, name_of_person2):
    return name_of_person2 in friends.get(name_of_person1, set())


def print_friends(name_of_person):
    if name_of_person in friends:
        print(" ".join(sorted(friends[name_of_person])))
    else:
        print()


add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))