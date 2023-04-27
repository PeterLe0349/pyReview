# use curly for sets avoid duplicates
vowels = {'a', 'e', 'i', 'o', 'u', 'u'}
found = []
word = input("Enter a word to check for vowels: ")
print(sorted(vowels.intersection(set(word))))