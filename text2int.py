def text2int(textnum, numwords={}):
    units = [
        "ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь",
        "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
        "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девянадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
            "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]

    if not numwords:
        for idx, word in enumerate(units):
            numwords[word] = (1, idx)
        for idx, word in enumerate(tens):
            numwords[word] = (1, idx*10)

    current = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Ошибка в слове либо слишком большое значение: " + word)
        multiplier, value = numwords[word]
        current = int(current) * int(multiplier) + int(value)
    return current