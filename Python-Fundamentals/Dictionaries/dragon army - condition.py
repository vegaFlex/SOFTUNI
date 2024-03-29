# Heroes III е най-добрата игра в историята. Всички я обичат и я играят постоянно.
#  Стамат не е изключение от това правило. Любимите му единици в играта са всички видове дракони
#  - черни, червени, златни, лазурни и т.н..
# Толкова ги харесва, че им дава имена и води дневници за статистиките им: щети, здраве и броня.
# Процесът на обобщаване на всички данни е доста досаден, затова би искал да има програма, която да го прави.
# Тъй като той не е програмист, твоята задача е да му помогнеш.

# Трябва да категоризирате драконите по техния тип.
# За всеки дракон, идентифициран по име, съхранявайте информация за статистиката му.

# Типът се запазва както при въвеждането, но драконите се подреждат по азбучен ред на имената.

#  За всеки тип трябва да отпечатате и средните щети, здравето и бронята на драконите.
#  За всеки дракон отпечатайте собствените му статистики.
# Възможно е обаче във входа да липсват статистики.
# Ако някоя статистика липсва, трябва да ѝ присвоите стойности по подразбиране.
# Стойностите по подразбиране са следните: здраве 250, щети 45 и броня 10.
# Липсващата статистика ще бъде отбелязана с null.

# Входът е в следния формат {тип} {име} {увреждане} {здраве} {броня}.
# На всяко от целите числа може да бъде присвоена нулева стойност.
#  Вижте примерите по-долу, за да разберете по-добре задачата си.

# Ако един и същ дракон бъде добавен втори път, новите статистики трябва да презапишат предишните.
# Два дракона се считат за равни, ако съвпадат по име и тип.
# Въвеждане на
# - На първия ред е дадено числото N -> броят на драконите, които трябва да се следват
# - На следващите N реда се въвеждат данни в описания по-горе формат. Всеки елемент ще бъде отделен с един интервал.
# Изход
# - Отпечатване на обобщените данни в конзолата
# - За всеки тип изведете средната статистика на неговите дракони във формат {Тип}::({увреждане}/{здраве}/{броня})
# - Щетите, здравето и бронята трябва да се закръглят до две цифри след десетичния разделител
# - За всеки дракон отпечатайте статистиките му във формат -{Име} -> щети: {увреждане}, здраве: {здраве}, броня: {броня}
# Ограничения
# - N е в интервала [1...100]
# - Типът и името на дракона са само една дума, започваща с главна буква.
# - Здравето и бронята са цели числа в интервала [0 ... 100000] или null

