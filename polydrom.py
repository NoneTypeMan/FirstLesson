while True:

    word = input('Введите слово, которое вы бы хотели проверить, является ли оно палиндромом, или нет: ')

    word_flip = word[::-1]

    if word == word_flip:
        print('Это палиндром!')

    else:
        print('Это не палиндром :(')
