library=[]
wishlist=[]
book_name=input('add a book to your library:')
library.append(book_name)
book_name=input('add another book to the library or Press Enter to skip:')
if book_name :
    library.append(book_name)
    print('your library :',library)
else:
    print('your library :',library)
book_name=input("\nadd a book you wish to have in the future:")
wishlist.append(book_name)
book_name=input('add another book you wish to have in the future or Press Enter to skip:')
if book_name:
    wishlist.append(book_name)
    print('your wishlist',wishlist)
else:
    print('your wishlist',wishlist)
acquired_book =input ("\nenter the name of a book from your wishlist that you have acquired or press enter to skip:")
if acquired_book:
   if acquired_book in wishlist:
      library.append(acquired_book)
      wishlist.remove(acquired_book)
      print ("updated library: ", library)
      print ("updated wishlist: ", wishlist)
   else:
      print (f"the book (acquired_book) is not in your wishlist")
else:
    print ("updated library: ",library)
    print ("updated wishlist: ", wishlist)

donated_book = input ("\nenter the name of a book from your library you wish to donate or press enter to skip:")
if donated_book:
   if donated_book in library:
      library.remove(donated_book)
      print ("final library after donations:", library)
   else:
      print (f"the book (donated_book) is not in your library")

else:
    print ("final library after donations:", library)