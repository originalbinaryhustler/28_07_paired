class GrammarStats:
    def __init__(self):
        self.punctuation = ['.','!','?']
        self.checks_made = 0
        self.checks_true = 0

    def check(self, text):
        if text == '' or not isinstance(text, str):
            raise Exception('Error: Instance type must be a string')
        elif text[0].isupper() and text[-1] in self.punctuation:
            self.checks_made += 1
            self.checks_true +=1
            return True
        self.checks_made += 1
        return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.checks_made == 0:
            return 0
        return 100 / self.checks_made * self.checks_true