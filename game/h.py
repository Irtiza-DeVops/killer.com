books = []
users = []

def add(book_id, title, author, genre, status='Available'):
    x = {'id': book_id, 'title': title, 'author': author, 'genre': genre, 'status': status}
    books.append(x)

def user(user_id, name):
    y = {'id': user_id, 'name': name, 'borrowed_books': []}
    users.append(y)

def all_books(items):
     
    for i in items:
        print(f'''{i['id']}. "{i['title']}" by {i['author']} (Genre: {i['genre']}, Status: {i['status']})''')
def all_users(items):
    for i in items:
        print(f"{i['id']}. {i['name']} .(Borrowed books: {i['borrowed_books']})")
def borrow_books(u_id,b_id):
    
    for borrower in users:
        if borrower['id'] == u_id:
          
           user = borrower
           break
    
    for x in books:
        if x['id'] ==b_id:
        
           book=x
           break
    if book['status']=='Available':
        book['status']='Check_out'
        user['borrowed_books'].append(book)
def return_book(u_id,b_id):
    for returner in users:
        if returner['id'] == u_id:
            user = returner
            break
    for x in books:
        if x['id'] == b_id:
            book = x
            break
    if book['status'] == 'Check_out':
        book['status'] ='Available'
        user['borrowed_books'].remove(book)
def searching(q):
    found_books=[]
    for x in books:
        if q in x['title'] :
            found_books.append(x)
    if found_books:
        print(found_books)

add("1", "To Kill a Mockingbird", "Harper Lee", "Fiction")
add("2", "1984", "George Orwell", "Dystopian")
add("3", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
add("4", "The Hobbit", "J.R.R. Tolkien", "Fantasy")
user("1", "Irtiza")
user("2", "Ali")
user("3", "Zaryan")


def main():
    while True:
        print("-------------------------------------------------------")
        print('''\n�� Welcome to the Community Library System! ���''')
        print("\nChoose an option:")
        print("1. View  all books")

        print("2. view all  users")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Search for a book")
        print("6. Exit")
        choice=input('enter your choice (1 ,6 ):' )
        
        if choice=='1':
            all_books(books)
        elif choice=='2':
            all_users(users)
        elif choice=='3':
            u_id=input('whats your id:')
            b_id=input('write book id : ')
            borrow_books(u_id,b_id)
        elif choice== '4':
            u_id=input('whats your id:')
            b_id=input('write book id : ')
            return_book(u_id,b_id)
        elif choice=='5':
            
            q=input("add title of book you want to search : ")
            if q :
                print(f"Searching for book with title : {q}")
                print(q)
                searching(q)
        elif choice =='6':
            print("Thank you for using our library system. Goodbye!")
            break
        else:
            print("Invalid option, please try again")
  
main()



    
        
