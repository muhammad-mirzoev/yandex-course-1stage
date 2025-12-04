history = []

def prompter(substring):
    for full_string in history:
        if substring in full_string:
            return full_string
    history.append(substring)
    return substring


print(prompter("Why do you cry, Willy?"))
print(prompter("Why, Willy?"))
print(prompter("Why do"))