volume = 1.44
volume_in_kbytes = volume * 1024
volume_in_bytes = volume_in_kbytes * 1024
count_symbols_in_page = 25 * 50
count_symbols_in_book = count_symbols_in_page * 100
volume_of_book = 4 * count_symbols_in_book
count_of_books = int(volume_in_bytes // volume_of_book)
print("Количество книг, помещающихся на дискету:", count_of_books)
