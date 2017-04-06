from tokenizer.Token import *

class OpToken(Token):
    def __init__(self, linen, start, orig):
        super().__init__(linen, start, orig)
        self.op = orig
