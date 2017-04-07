from tokenizer.Token import *

class KeywordToken(Token):
    def __init__(self, linen, start, orig):
        super().__init__(linen, start, orig)
        self.key = orig
