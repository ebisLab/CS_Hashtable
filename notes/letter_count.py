
# lets make a hashtalbe
# key is letter, and val is the


def print_letter_count(string):
    counts = {}  # dictionary

    for character in string:
        print(character)

    # common pattenrn
    for character in string:
        character = character.lower()  # case insensitive
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1

    print(counts)

    # i can also sort it too
    items = list(counts.items())
    items.sort(key=lambda e: e[1])
    # items.sort(key=lambda e: e[1], reverse=True)
    print(items)


print_letter_count("aaaabbbcc")
