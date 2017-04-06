from tokenizer.Token import *

class ErrorToken(Token):
    def __init__(self, linen, start, orig):
        super().__init__(linen, start, orig)
        self.err = orig
    
    def __str__(self):
        return 'ERROR:' + self.err
