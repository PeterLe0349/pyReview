book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print(booklist)
print(booklist[0:3])
print(''.join(booklist[0:3]))
print(''.join(booklist[-6:]))
backwards = booklist[::-1] 
print(''.join(backwards))
print(''.join(booklist[::2]))
new_book = ''.join(booklist[4:])
print(new_book)