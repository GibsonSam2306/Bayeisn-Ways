def palindrome():
    x = input('Enter a word: ')
    x_lower = x.lower()
    y_lower = x_lower[::-1]

    if x_lower == y_lower:
        print('True')
    else:
        print('False')
palindrome()