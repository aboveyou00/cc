from tokenizer.Token import *

class NumberToken(Token):
    def __init__(self, linen, start, orig):
        super().__init__(linen, start, orig)
        self.num = int(orig)
