def ordinal2int(textnum, gender, numwords={}):
    save_textnum = textnum
    textnum = textnum.replace('ё', 'е')
    if gender == 'femn':
        units = [
            "нулевая", "первая", "вторая", "третья", "четвертая", "пятая", "шестая", "седьмая", "восьмая",
            "девятая", "десятая", "одиннадцатая", "двенадцатая", "тринадцатая", "четырнадцатая",
            "пятнадцатая", "шестнадцатая", "семнадцатая", "восемнадцатая", "девянадцатая"]
        tens0 = ["", "", "двадцатая", "тридцатая", "сороковая", "пятидесятая",
                "шестидесятая", "семидесятая", "восьмидесятая", "девяностая"]
        tens1 = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
                "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
        hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    elif gender == 'masc':
        units = [
            "нулевой", "первый", "второй", "третий", "четвертый", "пятый", "шестой", "седьмой", "восьмой",
            "девятый", "десятый", "одиннадцатый", "двенадцатый", "тринадцатый", "четырнадцатый",
            "пятнадцатый", "шестнадцатый", "семнадцатый", "восемнадцатый", "девянадцатый"]
        tens0 = ["", "", "двадцатый", "тридцатый", "сороковой", "пятидесятый",
                "шестидесятый", "семидесятый", "восьмидесятый", "девяностый"]
        tens1 = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят",
                "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
        hundreds = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    
    llist = [tens0, tens1]
    
    for item in textnum.split():
        if item in hundreds:
            to_add = item
            indexx = textnum.split().index(item)
            textnum = ' '.join(textnum.split()[indexx+1:])
            break
        else:
            to_add = None
    
    if textnum.split()[0] not in hundreds:
        if len(textnum.split()) > 1:
            ind = 1
        elif len(textnum.split()) == 1:
            ind = 0    
        if not numwords:
            for idx, word in enumerate(units):
                numwords[word] = (1, idx)
            for idx, word in enumerate(llist[ind]):
                numwords[word] = (1, idx*10)
            if to_add is not None:
                for idx, word in enumerate(hundreds):
                    numwords[word] = (1, idx*100)
        current = 0
        for word in textnum.split():
            try:
                multiplier, value = numwords[word]
                current = int(current) * int(multiplier) + int(value)
            except:
                continue
        if to_add is not None:
            multiplier, value = numwords[to_add]
            current += value

    if current == 0:
        return save_textnum
    else:    
        return current            
