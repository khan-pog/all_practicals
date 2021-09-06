"""A program to count the occurrences of words in a string."""

test_string = (
    'this is a collection of words of nice words this is a fun thing it is')
parts = test_string.split()
word_to_count = {}
count_to_word = {}

for word in parts:  # DONE: FIND THE LONGEST WORD
    for part in parts:
        count_to_word[len(part)] = part
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

print("{:{}} = {}".format(word, max(count_to_word),
                          word_to_count[word]))  # DONE: FORMAT THE LIST
