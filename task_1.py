print('Задача 1. Я стал новым пиратом!')

# Старому капитану нужно пополнить команду, но на корабль попадут только достойные! Он отобрал десять человек. Те, кто крикнет слово «Карамба», попадут на борт.

# Что нужно сделать

# Пользователь вводит десять слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».

count = 0

for i in range(1, 10 + 1):
  word = input("Введите " + str(i) + "-ое слово: ")
  if word == "Карамба" or word == "карамба":
    count += 1
  
print(f"Совпадений: {count}")
