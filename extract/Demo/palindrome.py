# word = input("Enter word: ").lower()
# reverse_word = ""

# for i in word:
#     reverse_word = i + reverse_word

# if reverse_word == word:
#     print(f"The word {word} is a palindrome")

# else:

#     print(f"The word {word} is NOT a palindrome")

def palindrome():
    word = input("Enter word: ").lower()
    if word == word[::-1]:
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")


palindrome()
