vowels = set('aeiou')
word = 'sdfaslkfjwer2'
ulist = vowels.union(set(word))
# print(vowels)
# print(set(word))
# print(sorted(ulist))
diflist = vowels.difference(set(word))
interlist = vowels.intersection(set(word))
# print(sorted(diflist))
print(sorted(interlist))