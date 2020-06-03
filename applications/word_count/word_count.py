import string


def word_count(s):
    # Your code here
    counts = {}  # dictionary

# remove punctuation
    for char in '":;,.-+=/|[]{}()*^\&':
        s = s.replace(char, '')

# split the words
    words = s.split()

    for word in words:
        word = word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

    print(counts)


if __name__ == "__main__":
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
