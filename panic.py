phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop(3)
for x in range(4):
    plist.pop()
plist.pop(0)
plist.insert(3,plist.pop(2))
plist.append(plist.pop(4))



new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

#test