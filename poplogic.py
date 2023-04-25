phrase = "123456789"
plist = list(phrase)
print(plist)
#store all the pops in list then extend it in order it was popped
plist.extend([plist.pop(),plist.pop(),plist.pop()])
print(plist)
print(''.join(plist))



word = "i can't eat zebras but won't listen"
print(word)
wlist = list(word)
wlist.remove("'")
print(''.join(wlist))