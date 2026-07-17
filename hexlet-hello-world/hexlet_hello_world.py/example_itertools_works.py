from more_itertools import sliced, substrings

# Генерируем все подстроки слова "more"
subs = ["".join(s) for s in substrings("more")]
print("Подстроки:", subs)

# Разбиваем кортеж на части по 3 элемента
slices = list(sliced((1, 2, 3, 4, 5, 6, 7, 8), 3))
print("Срезы:", slices)
