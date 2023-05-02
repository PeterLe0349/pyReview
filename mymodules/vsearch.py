import os

def search4vowels(phrase:str) -> set:
    """Displays any vowels found in asked-for word."""
    vowels = set("aeiou")
    # word = input("Enter a word to check for vowels: ")
    return vowels.intersection(set(phrase))
    # for vowel in sorted(found):
    #     print(vowel)


def search4letters(phrase:str, letters:str='aeiou') -> set:
    return set(letters).intersection(set(phrase))

# print(search4letters('life, the iniverse, and everything'))
# print(search4letters('life, the universe, and everything', 'oae'))
# print(search4letters(letters='wx', phrase='whats up xxfolk'))


# print(type(os.getcwd()))