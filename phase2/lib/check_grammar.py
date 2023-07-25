def check_grammar(text):
    if text == '':
        return False
    else:
        if text[0].islower():
            return False
        else:
            if text[-1] != '!' and text[-1] != '.':
                return False
            else:
                return True