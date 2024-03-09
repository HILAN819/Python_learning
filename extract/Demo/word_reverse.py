word = input("Input a word to reverse: ")
# reverse_word = word[::-1]
# print(reverse_word)
for i in range(len(word)-1, -1, -1):
    print(word[i], end='')

print("\n")
