__author__ = 'drzewko'

word = raw_input("Input a word\n")
word_length = len(word)
reverse_word = ""
for i in range(word_length):
    reverse_word += word[word_length - i - 1]

print reverse_word
