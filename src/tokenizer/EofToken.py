from tokenizer.Token import *

class EofToken(Token):
    def __init__(self, linen, start, orig):
        super().__init__(linen, start, orig)
    
    def __str__(self):
        return 'EOF'
