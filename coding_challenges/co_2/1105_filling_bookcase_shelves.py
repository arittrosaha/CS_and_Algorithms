# https://leetcode.com/problems/filling-bookcase-shelves/

def min_height_shelves(books, shelf_width): # Time: O(n) ; Space: O(1)
    min_height = 0
    current_shelve_h, current_shelve_w = 0, 0
    for book in books:
        current_book_w, current_book_h = book[0], book[1]
        if current_book_w + current_shelve_w > shelf_width:
            min_height += current_shelve_h
            current_shelve_h, current_shelve_w = 0, 0
        current_shelve_w += current_book_w
        if current_book_h > current_shelve_h: current_shelve_h = current_book_h
    return min_height


print(min_height_shelves(
    [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]],
    4
    )) # => 6

