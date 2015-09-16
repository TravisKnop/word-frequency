import re
import string

with open("sample.txt") as infile:
    lower_text = infile.read()
clean_text = re.sub("[^a-zA-Z, ]+", "", lower_text)
word_list = clean_text.split(' ')

word_dictionary = {}

for word in word_list:
    if word in word_dictionary.keys():
        word_dictionary[word] += 1
    else:
        word_dictionary[word] = 1

list_word_value = []

for text, frequency in word_dictionary.items():
    temp = [text,frequency]
    list_word_value.append(temp)

final_list = sorted(list_word_value, key=lambda x: x[1], reverse=1)

i = 0
for x, y in final_list:
    if i < 20:
        print(x + ": ",y)
        i += 1
