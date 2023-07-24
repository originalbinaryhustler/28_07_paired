
def make_snippet(string):
    if len(string.split()) > 5:
        string_list = string.split()
        list_first_five = string_list[0:5]
        return f"{' '.join(list_first_five)}..."
    else: 
        return string 