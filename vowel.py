vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Give me some word, to find into vowels: \n')
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found:
    print(vowels)
