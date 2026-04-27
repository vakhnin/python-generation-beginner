most_heavy_word = ""
most_heavy_word_value = 0

for _ in range(4):
    current_word = input()
    current_word_value = 0
    for char in current_word:
        current_word_value += ord(char)
    if current_word_value > most_heavy_word_value:
        most_heavy_word = current_word
        most_heavy_word_value = current_word_value

print(most_heavy_word)
