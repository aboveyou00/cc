

class Syntax(object):
    def __init__(self, cunit, tok_start_idx, tok_count):
        super().__init__()
        self.cunit = cunit
        self.tok_start_idx = tok_start_idx
        self.tok_count = tok_count
    
    def __str__(self):
        toks = self.cunit.tokens[self.tok_start_idx : self.tok_start_idx+self.tok_count]
        print(toks)
        return ' '.join(map(str, toks))
