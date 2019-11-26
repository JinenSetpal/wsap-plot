from matplotlib import pyplot as plt
import sys

lines = []
try:
    lines = open(sys.argv[1]).readlines()
except IOError:
    sys.exit("Error: Path incorrect or file non-existent\nExiting program.")
dict = {}
count = 1
len_lines = len(lines)
temp_dict = {}
date = [lines[0][3:8], ]

while len(lines) > 0:
    j = lines[0]
    try:
        n = int(j[0:2]) + int(j[3:5]) + int(j[6:8])
        if j[2] != j[5] and j[8] != ",":
            print("Parsed line", count, "of", len_lines)
            count += 1
            lines.pop(0)
            continue
    except ValueError:
        print("Parsed line", count, "of", len_lines)
        count += 1
        lines.pop(0)
        continue
    if j[3:5] != date[-1][0:2]:
        date.append(j[3:8])
        for j in temp_dict:
            try:
                dict[j].extend([0, ] * (len(date) - len(dict[j]) - 2))
                dict[j].append(temp_dict[j])
            except KeyError:
                dict[j] = [0, ] * (len(date) - 2)
                dict[j].append(temp_dict[j])
        temp_dict.clear()
    else:
        lines.pop(0)
        print("Parsed line", count, "of", len_lines)
        count += 1
        if j.find(": ") == -1:
            continue
        try:
            temp_dict[j[j.index("-") + 2:j.index(": ")]] += 1
        except KeyError:
            temp_dict[j[j.index("-") + 2:j.index(": ")]] = 1
if len(date) == 1:
    print("This program plots over months. The provided chat has not yet crossed a month.")
else:
    for i in dict:
        if len(dict[i]) <= 7:
            dict[i].extend([0, ] * (8 - len(dict[i])))
        plt.plot(date, dict[i], label=i)
    plt.legend()
    plt.show()
