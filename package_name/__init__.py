def capitalize(text):
    for char in text:
        result = char.upper()
        return f'{result}{text[1:]}'
    return text