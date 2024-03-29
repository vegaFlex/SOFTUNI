# Разполагате с много свободно време и решавате да напишете програма,
# която скрива и разкрива получените съобщения. Започнете да я въвеждате!

# На първия ред на входа ще получите скритото съобщение.

# След това, докато не бъде подадена командата "Разкриване",
# ще получавате низове с инструкции за различни операции,
# които трябва да се извършат върху скритото съобщение,
# за да се интерпретира то и да се разкрие действителното му съдържание.

# Съществуват няколко вида инструкции, разделени с ":|:"
# - "InsertSpace:|:{index}":
# o Вмъква единичен интервал в дадения индекс. Даденият индекс винаги е валиден.
# o
# - "Reverse:|:{substring}":
# o Ако съобщението съдържа дадения подниз, изрязва го, обръща го и го добавя в края на съобщението.
# o Ако не е, отпечатайте "грешка".
# o Тази операция трябва да замени само първата поява на дадения подниз, ако има две или повече появявания.

# - "ChangeAll:|:{substring}:|:{replacement}":
# o Променя всички срещания на дадения подниз с текста за замяна.

# Входни данни / Ограничения
# - На първия ред ще получите низ със съобщение.
# - На следващите редове ще получавате команди, разделени с ":|:".
# Изход
# - След всеки набор от инструкции отпечатайте получения низ.
# - След получаване на командата "Reveal" (Разкриване), отпечатайте това съобщение:
# "Имате ново текстово съобщение: {съобщение}"
