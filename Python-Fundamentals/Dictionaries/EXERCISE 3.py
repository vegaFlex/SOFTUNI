# Познавате системата "Джуд", нали?! Вашата задача е да създадете програма, подобна на системата "Джъд".
# Ще получите няколко входни реда в един от следните формати:
# {име} -> {състезание} -> {точки}

# КонтестНаимето и потребителското име са низове, а зададените точки ще бъдат цяло число.
# Трябва да следите всяко състезание и индивидуалната статистика на всеки потребител.

# Трябва да проверите дали такова състезание вече съществува и ако не, да го добавите,
# в противен случай да проверите дали настоящият потребител участва в състезанието,
# ако участва, вземете по-високата оценка, в противен случай просто го добавете.

# Също така трябва да поддържате индивидуална статистика за всеки потребител - общия брой точки от всички контести.

# Трябва да прекратите програмата си, когато получите командата "no more time" (няма повече време).

# В този момент трябва да отпечатате всеки конкурс по реда на въвеждане, за всеки конкурс да отпечатате участниците,
# подредени по точки в низходящ ред, а след това подредени по име във възходящ ред.

# След това трябва да отпечатате индивидуални статистически данни за всеки участник, подредени по общ брой точки в низходящ ред,
# а след това по азбучен ред.

# Входни данни / ограничения
# - Входните данни са под формата на команди в един от посочените по-горе формати.
# - Потребителското име и името на състезанието винаги ще бъдат една дума.
# - Точките ще бъдат цяло число ще бъдат цяло число в диапазона [0, 1000].
# - Няма да има невалидни входни редове.
# - Ако всички критерии за сортиране са неуспешни, подреждането трябва да бъде по реда на въвеждане.
# - Въвеждането на данни приключва, когато се получи командата "няма повече време".

# Изход
# - Форматът на изхода за конкурсите е:
# {име на конкурса}: {participants.Count} участници
# {позиция}. {име на потребителя} <::> {точки}
# - След като отпечатате всички конкурси, отпечатайте индивидуалната статистика за всеки участник.
# - Форматът на изхода е:
# Индивидуална класация:
# {позиция}. {име на потребителя} -> {общоточки}