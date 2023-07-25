
def make_snippet(text):
    if isinstance(text, str):
        if len(text.split()) > 5:
            text_list = text.split()
            list_first_five = text_list[:5]
            return f"{' '.join(list_first_five)}..."
        else: 
            return text
    else:
        raise Exception('Error: Input was not a string.')

def count_words(text):
    if isinstance(text, str):
        text_list = text.split()
        return len(text_list)
    else:
        raise Exception('Error: Input was not a string.')