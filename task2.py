N = int(input("скільки слів?"))

words = []

for i in range(N):

    word = input("Ведіть слово:")

    words.append(word)

spaced_words = []

for word in words:

    space_word = " ".join(word)
    spaced_words.append(space_word)

result = ", ".join(spaced_words)

print(result)




