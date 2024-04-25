import random


def generate_letter_grid(words, grid_size=4):
    # Собираем все буквы из выбранных слов
    all_letters = ''.join(words)

    # Проверяем, хватает ли букв для заполнения сетки
    if len(all_letters) < grid_size ** 2:
        raise ValueError("Недостаточно букв для заполнения сетки")

    # Разбиваем строку на список букв и перемешиваем
    letters_list = list(all_letters)
    random.shuffle(letters_list)

    # Формируем таблицу букв размером grid_size x grid_size
    grid = [letters_list[i * grid_size:(i + 1) * grid_size] for i in range(grid_size)]

    return grid


# Пример списка слов
words_list = ["апельсин", "мандарин", "лимон", "грейпфрут"]

# Выбираем случайные слова из списка, пока не соберем достаточно букв
selected_words = []
letters_collected = 0
while letters_collected < 16:
    word = random.choice(words_list)
    if word not in selected_words:
        selected_words.append(word)
        letters_collected += len(word)

# Генерируем таблицу букв
letter_grid = generate_letter_grid(selected_words)

# Вывод таблицы для проверки (комментирование для финального кода)
for row in letter_grid:
    print(' '.join(row))

while selected_words:
    print("Введите загаданное слово")
    user_answer = input()

    if user_answer in selected_words:
        print("Вы угадали")
        selected_words.remove(user_answer)
    else:
        print("Вы не угадали")
print("Поздравляем вы угадали все слова")
