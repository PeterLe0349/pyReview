phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop(3)
plist.pop(0)
plist.insert(5,plist.pop(2))



new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

#test