vowels = ['a', 'e', 'i', 'o', 'u']
found = {}
for vowel in vowels:
    if vowel not in found:
        found[vowel] = 0

word = input("Enter a word to check for vowels: ")
for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found ', v, 'time(s)')
    