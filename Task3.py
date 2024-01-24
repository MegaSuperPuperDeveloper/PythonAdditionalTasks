# Сделать игру "Очко", 11 карт от 1 до 11, которые не повторяются
import random
import os

def print_cards(your_cards, his_cards):
    res1 = ""
    res = ""
    print()
    print("Твои карты:")
    for i in your_cards:
        res1 += str(i) + " "
    print(res1)
    print()
    print("Его карты:")
    for i in his_cards:
        if i == his_cards[0]:
            res += "* "
        else:
            res += str(i) + " "
    print(res)

your_res = ""
his_res = ""
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
your_cards = []
his_cards = []
length = len(cards)
for i in range(4):
    a = random.randint(0, len(cards) - 1)
    if i <= 1:
        his_cards.append(cards[a])
    else:
        your_cards.append(cards[a])
    cards.remove(cards[a])

while True:
    sum = 0
    his_sum = 0
    print_cards(your_cards, his_cards)
    input()
    print("Братк, что делаем? Пас/Берем карту")
    print("1. Пас")
    print("2. Берем карту")
    ans = int(input())
    if ans == 2 and len(cards) != 0:
        for i in your_cards:
            sum += i
        if sum < 21:
            a = random.randint(0, len(cards) - 1)
            your_cards.append(cards[a])
            cards.remove(cards[a])
    for i in his_cards:
        his_sum += i
    if his_sum < 15:
        a = random.randint(0, len(cards) - 1)
        his_cards.append(cards[a])
        cards.remove(cards[a])
    elif ans == 1 or sum > 21:
        break
    if his_sum > 21 and sum > 21:
        break
    else:
        sum = 0
        his_sum = 0
print()
for i in your_cards:
    your_res += str(i) + " "
print("Твои карты:")
print(your_res)
print()
for i in his_cards:
    his_res += str(i) + " "
print("Его карты:")
print(his_res)
print()
if his_sum > 21 and sum < 22:
    print("Ты победил этого чушпана!")
elif his_sum < 22 and sum > 21:
    print("Тебя победили, братк")
elif his_sum == sum:
    print("Ничья")
elif his_sum < 22 and sum < 22 and his_sum > sum:
    print("Тебя победили, братк")
elif his_sum < 22 and sum < 22 and sum > his_sum:
    print("Ты победил этого чушпана!")
elif his_sum > 21 and sum > 21 and his_sum > sum:
    print("Тебя победили, братк")
elif his_sum > 21 and sum > 21 and sum > his_sum:
    print("Ты победил этого чушпана!")