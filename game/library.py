# books = []
# users = []

# def add(book_id, title, author, genre, status='Available'):
#     x = {'id': book_id, 'title': title, 'author': author, 'genre': genre, 'status': status}
#     books.append(x)

# def user(user_id, name):
#     y = {'id': user_id, 'name': name, 'borrowed_books': []}
#     users.append(y)

# def all_books():
#     print(''' 
#          📚 All Books 📚:''')
#     for i in books:
#         print(f'''{i['id']}. "{i['title']}" by {i['author']} (Genre: {i['genre']}, Status: {i['status']})''')
      
# def searching(s):
#     found_books = []
    
#     for b in books:
#         if s in b['title']:
#             found_books.append(b)

#     if found_books:
#         print('''\n🔍 Search Results:''')
#         for m in found_books:
#             print(f'''{m['id']}. "{m['title']}" by {m['author']} (Genre: {m['genre']}, Status: {m['status']})''')
#     else:
#         print("🚫 No matching books found.")

# def borrow_book(user_id, book_id):
#     user = None
#     for borrower in users:
#         if borrower['id'] == user_id:
#             user = borrower
#             break

#     book = None
#     for borrowed in books:
#         if borrowed['id'] == book_id:
#             book = borrowed
#             break

#     if user is None:
#         print("🚫 Invalid User ID.")
#         return
   
#     if book is None:
#         print("🚫 Invalid Book ID.")
#         return
    
#     if book['status'] == 'Available':
#         book['status'] = 'Checked Out'  
#         user['borrowed_books'].append(book)  
#         print(f'''✅ You have borrowed "{book['title']}".''')
#     else:
#         print(f'''🚫 Sorry, the book "{book['title']}" is currently checked out.''')

# def returning(user_id, book_id):
#     user = None
#     for returner in users:
#         if returner['id'] == user_id:
#             user = returner
#             break

#     book = None
#     for r_book in books:
#         if r_book['id'] == book_id:
#             book = r_book
#             break

#     if user is None:
#         print("🚫 Invalid User ID.")
#         return
   
#     if book is None:
#         print("🚫 Invalid Book ID.")
#         return
    
#     if book in user['borrowed_books']:
#         user['borrowed_books'].remove(book)  
#         book['status'] = 'Available'
#         print(f'''✅ You have returned "{book['title']}".''')
#     else:
#         print(f'''🚫 Sorry, you cannot return "{book['title']}" as it was not borrowed by you.''')
    
# def all_users():
#     print('''\n👥 All Users:''')
#     for user in users:
#         print(f"{user['id']}. {user['name']} .(Borrowed books:{user['borrowed_books']})")
        
        
    

# add("1", "To Kill a Mockingbird", "Harper Lee", "Fiction")
# add("2", "1984", "George Orwell", "Dystopian")
# add("3", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
# add("4", "The Hobbit", "J.R.R. Tolkien", "Fantasy")
# user("1", "Irtiza")
# user("2", "Ali")
# user("3", "Zaryan")

# def main():
#     while True:
#         print("-------------------------------------------------------")
#         print('''\n🌟 Welcome to the Community Library System! 🌟''')
#         print("--------------------------------------------------------")
#         print('''\nPlease choose an option:
#         1. View all books
#         2. Search for a book
#         3. Borrow a book
#         4. Return a book
#         5. View all users
#         6. Exit
#               ''')

#         chose = input('''Enter your choice (1-6): ''')

#         if chose == '1':
#             all_books()
#         elif chose == '2':
#             searching(input("Enter the exact title of the book: "))
#         elif chose == '3':
#             user_id = input("Enter your User ID: ")
#             book_id = input("Enter the Book ID you want to borrow: ")
#             borrow_book(user_id, book_id)
#         elif chose == '4':
#             user_id = input("Enter your User ID: ")
#             book_id = input("Enter the Book ID you want to return: ")
#             returning(user_id, book_id)
#         elif chose == '5':
#             all_users()
#         elif chose == '6':
#             print("🌈 Exiting the system. Goodbye! 🌈")
#             break
#         else:
#             print("🚫 Invalid choice. Please try again.")

# main()
