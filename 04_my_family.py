#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['father', 'mather', 'sister', 'brother']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['father', 180],
    ['mother', 165],
    ['sister', 164],
    ['brother', 166]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(my_family_height[0][0])
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum = 0
i = 0
while i != len(my_family_height):
    sum = sum + my_family_height[i][1]
    i += 1
print(sum)