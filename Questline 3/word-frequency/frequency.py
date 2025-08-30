
text = input("Enter a paragraph: ")
words = text.lower().split()
word_counts = {}
for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    if word:
        word_counts[word] = word_counts.get(word, 0) + 1
for word, count in word_counts.items():
    print(f"{word} → {count}")
