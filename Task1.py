# Сделать программу которая записывает слова задом наперед
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

word = input("Введите слово: ")
index = 0
new_word = list()
length = len(word)
new_word = [i for i in range(length)]
for i in word:
    if i == " ":
        print("Ошибка! Надо написать слово!")
while index < length:
    new_word[index] = word[length - 1 - index]
    index += 1
new_word = "".join(new_word)
print(f"'{word}' => '{new_word}'")