# caesar cipher
# big subsitution table

# BEEJ => ZOOT
encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}


# def encode(string):
#     result = ""
#     for character in string:

#         result += encode_table[character]
#     return result

# accounting for punctuations
def encode(string):
    result = ""
    for character in string:
        if character in encode_table:
            result += encode_table[character]
        else:
            result += character
    return result


print('encode~~>', encode("WEEEELOWORLD"))

# handling punctuation
print('encode w punctuation~~>', encode("WEEEEL,OWORLD!"))


decode_table = {}
decode_table2 = {}


def build_decode_table():
    for key, value in encode_table.items():
        decode_table2[value] = key
    # for key in encode_table:
    #     value = encode_table[key]


def decode(string):
    result = ""
    for character in string:
        result += decode_table2[character]
    return result


build_decode_table()
print('decode ~~~>', decode("BOOOOGEBEUGW"))

