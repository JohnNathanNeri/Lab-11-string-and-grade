Words = []
words_to_be_printed = []
while len(Words)!=10:
    ten_words = input("Enter a word: ")
    Words.append(ten_words)
    
length = int(input(""))
for word in Words:
    if len(word) >= length:
        words_to_be_printed.append(word)
        continue
print(words_to_be_printed)