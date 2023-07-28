class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        no_vowels = []
        for i in range(len(self.text)):
            if self.text[i].lower() not in self.vowels:
                no_vowels.append(self.text[i])
        return ''.join(no_vowels)
        # i = 0
        # while i < len(self.text):
        #     if self.text[i].lower() in self.vowels:
        #         self.text = self.text[1:]
        #     i += 1
        # return self.text
    
remover = VowelRemover("aeiou")
remover.remove_vowels()