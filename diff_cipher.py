def dif_ciph(words):
    first_loop = True
    if type(words) == str:
        new_words = []
        for item in words:
            item = ord(item)
            if first_loop == True:
                new_item = item
                first_loop = False
            else:
                new_item = item - last_item
            last_item = item
            new_words.append(new_item)
        return new_words
    else:
        new_string = ""
        for item in words:
            if first_loop == True:
                item = chr(item)
                new_item = item
                last_item = ord(item)
                first_loop = False
            else:
                new_item = item + last_item
                new_item = chr(new_item)
                last_item = ord(new_item)
            new_string += new_item
        return new_string
