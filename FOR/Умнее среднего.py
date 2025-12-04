n = int(input())

total_sum = 0
count = 0

for i in range(n):
    iq = int(input())

    if count == 0:
        print(0)
    else:
        average_iq = total_sum / count

        if iq > average_iq:
            print(">")
        elif iq < average_iq:
            print("<")
        else:
            print("0")

    total_sum += iq
    count += 1
