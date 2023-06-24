while True:

    word = input('Введите слово: ')

    word_flip = word[::-1]

    if word == word_flip:
        print('Это палиндром!')

    else:
        print('Это не палиндром :(')