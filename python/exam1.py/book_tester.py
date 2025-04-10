from book import Book

with open("books.txt") as file:
    books=[]
    for line in file:
        info=line.strip().split(",")
        title=info[0]
        author=info[1]
        genre=info[2]
        book1=Book(title,author,genre)
        books.append(book1)
    
    print(books[0].get_title())
    print(books[0].get_author())
    print(books[0].get_genre())
    print(books[0].is_checked_out())
    books[0].check_out()
    print(books[0])
    books[0].return_book()
    print(books[0])

