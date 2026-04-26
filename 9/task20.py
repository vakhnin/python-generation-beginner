string = input()

a, g, = string.upper().count("А"), string.upper().count("Г")
c, t = string.upper().count("Ц"), string.upper().count("Т")

print("Аденин:", a)
print("Гуанин:", g)
print("Цитозин:", c)
print("Тимин:", t)
