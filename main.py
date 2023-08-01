# 1
value1 = input("Введите слово: ")
value2 = ''.join(reversed(value1))
if value1==value2:
    print(value1, "является палиндромом")
else:
    print(value1, "не является палиндромом")

# 2
value3 = input("Введите текст: ")
words = input("Введите слово для замены: ").split()
for word in words:
    value3 = value3.replace(word, word.upper())
print(value3)

# 3
s = input("Введите текст: ")
print("Колличество предложений в введенном тексте: ", sum(s.count(x) for x in ('.!?')))

