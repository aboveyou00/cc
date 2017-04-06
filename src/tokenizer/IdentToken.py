from tokenizer.Token import *

class IdentToken(Token):
    def __init__(self, linen, start, orig):
        super().__init__(linen, start, orig)
        self.ident = orig
