letter_map = {
    'A': [
        " *  ",
        "* * ",
        "*** ",
        "* * ",
        "* * "
    ],
    'B': [
        "**  ",
        "* * ",
        "**  ",
        "* * ",
        "**  "
    ],
    'C': [
        " *  ",
        "* * ",
        "*   ",
        "* * ",
        " *  "
    ]
}

input_str = input().strip()

result = ["", "", "", "", ""]

for char in input_str:
    letter = letter_map[char]
    for i in range(5):
        result[i] += letter[i] + " "

for line in result:
    print(line.rstrip())
