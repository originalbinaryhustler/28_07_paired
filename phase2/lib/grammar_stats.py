class GrammarStats:
    def __init__(self):
        self.punctuation = ['.','!','?']
        self.checks_made = 0
        self.checks_true = 0
  
    def check(self, text):
        if text == '' or not isinstance(text, str):
            return False
        elif text[0].isupper() and text[-1] in self.punctuation:
            return True
        return False
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass