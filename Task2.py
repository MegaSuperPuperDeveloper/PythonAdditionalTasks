# Написать программу, которая замазывает все символы в строке кроме последних четырех
# Если символов меньше пяти, то ничего замазывать не надо

def maskify(word, length):
    length1 = length - 4
    list1 = list()
    print(length1 * '#' + word[length - 4] + word[length - 3] + word[length - 2] + word[length - 1])

word = input("Напишите набор символов: ")
length = len(word)
if len(word) < 5:
    print(f'"{word} --> {word}"')
else:
    maskify(word, length)