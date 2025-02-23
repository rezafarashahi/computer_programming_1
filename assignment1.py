


sentence = input("Enter a sentence: ")
sentence_lower = sentence.lower()

i_letter = 'i'
i_count = 0

for letter in sentence_lower:
    if letter == i_letter:
        i_count = i_count + 1

print(f"i has been used {i_count} times in the sentence.")