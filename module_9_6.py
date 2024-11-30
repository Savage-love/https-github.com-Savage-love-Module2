def all_variants(text):
    for i in range(len(text)):
        yield text[i]  # Отдельные символы
        for j in range(i + 1, len(text)):
            current_substring = text[i:j+1]
            yield current_substring


a = all_variants("abc")
for i in a:
    print(i)