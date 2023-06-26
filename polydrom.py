def checkPalindrome(word : str):

    word_flip = word.lower()[::-1]

    if word.lower().replace(" ", "") != word.lower():
        return "Напишите без пробелов"

    if word.lower() == word_flip:
        return True

    else:
        return False
    
while True:
    print(checkPalindrome(input('Введите слово, которое вы бы хотели проверить, является ли оно палиндромом, или нет: ')))
