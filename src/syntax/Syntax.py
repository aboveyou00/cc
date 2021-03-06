

class Syntax(object):
    def __init__(self, cunit, tok_start_idx, tok_count):
        super().__init__()
        self.cunit = cunit
        self.tok_start_idx = tok_start_idx
        self.tok_count = tok_count
    
    def registerNames(self, declspace):
        pass
    
    def resolveNames(self):
        pass
    
    def __str__(self):
        toks = self.cunit.tokens[self.tok_start_idx : self.tok_start_idx+self.tok_count]
        return ' '.join(map(str, toks))
