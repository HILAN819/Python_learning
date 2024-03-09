# from pprint import pprint
sentence = "This is a common interview question"
# for i in sentence:
#     sentence.count(i)
#     print(sentence.count(i))

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# pprint(char_frequency)

char_frequency_sorted = (sorted(char_frequency.items(), key=lambda kv:kv[1], reverse=True))
print("The most repeated character in the sentence is ", char_frequency_sorted[0])