def check_grammar(text):
    if isinstance(text,str):
        if text == '':
            return False
        else:
            if text[0].isupper():
                if text[-1] == '!' or text[-1] == '.':
                    return True
                else:
                    return False
            else:
                return False
    else:
        raise Exception("Error: input not a string")
