library = []
wishlist = []



# Library Books
library_book_1 = input("Enter the name of a book you own: ")
while library_book_1 == "":
  print("sorry, you must enter a book name")
  library_book_1 = input("Enter the name of a book you own: ")
if library_book_1:
  library.append(library_book_1)
library_book_2 = input("Enter the name of another book you own (or press 'Enter' to skip")
if library_book_2:
  library.append(library_book_2)
print(f"Your library: {library}")




# Wishlist Books
wishlist_book_1 = input("Enter the name of a book you wish to have in the future: ")
while wishlist_book_1 == "":
  wishlist_book_1 = input("Please enter the name of a book you wish to have in the future: ")
if wishlist_book_1:
  wishlist.append(wishlist_book_1)
wishlist_book_2 = input("Enter the name of another book you wish to have in the future: ")
if wishlist_book_2:
  wishlist.append(wishlist_book_2)
print(f"Your wishlist: {wishlist}")




# Acquired Books
acquired_book = input("Enter a name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")
while acquired_book not in wishlist:
  print("Sorry, this book is not in your wishlist")
  acquired_book = input("Enter a name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if acquired_book in wishlist:
  library.append(acquired_book)
  wishlist.remove(acquired_book)
  print(f"Updated Library: {library}")
  print(f"Updated Wishlist: {wishlist}")




# Donate Books
donate_book = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
while donate_book not in library:
  print("Sorry, this book is not in your library")
  donate_book = input("Please enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
if donate_book in library:
  library.remove(donate_book)
  print(f"Updated Library: {library}")



  