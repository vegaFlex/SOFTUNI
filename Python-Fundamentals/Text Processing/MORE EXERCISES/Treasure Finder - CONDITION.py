# Напишете програма,
# която декриптира съобщение по зададен ключ и събира информация за вида на скритото съкровище и неговите координати.

# На първия ред ще получите ключ (последователност от числа, разделени с интервал).
# На следващите няколко реда, докато получите "find", ще получите редове от низове.

# Трябва да преминете през всеки низ
# и да намалите ascii кода на всеки символ със съответното число от ключовата последователност.

# Начинът, по който избирате номера на ключа от последователността, е просто циклично преминаване през нея.
# Ако дължината на ключовата последователност е по-малка от последователността на низа,
# започвате цикъла от началото на ключа.

# За повече разяснения вижте примера по-долу.
# След декриптиране на съобщението ще получите вида на съкровището и неговите координати.
# Типът ще бъде между символа "&", а координатите ще бъдат между символите "<" и ">".
# За всеки ред отпечатайте типа и координатите във формат "Found {type} at {coordinates}".
