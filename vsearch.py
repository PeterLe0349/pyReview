def search4vowels(word):
    """Displays any vowels found in asked-for word."""
    vowels = set("aeiou")
    # word = input("Enter a word to check for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in sorted(found):
        print(vowel)


# search4vowels('bateman')
# search4vowels('mouse')
