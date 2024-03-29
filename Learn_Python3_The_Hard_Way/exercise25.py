# Using Library ex25 to convert string to list
import ex25

# String
sentence = "All good things come to those who wait."

# Operation on string using ex25
words = ex25.break_words(sentence)
print(words)
sorted_words = ex25.sort_word(words)
print(sorted_words)
ex25.print_first_word(words)
ex25.print_last_word(words)
print(words)
ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
print(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print(sorted_words)
ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)