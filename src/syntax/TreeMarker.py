from tokenizer import IdentToken, OpToken, NumberToken, EofToken

class TreeMarker(object):
    def __init__(self, cunit):
        super().__init__()
        self.cunit = cunit
        self.tokens = cunit.tokens
        self.pos = 0
    
    def mark(self):
        return self.pos
    
    def reset(self, mark):
        self.pos = mark
    
    def argsFrom(self, mark):
        return (self.cunit, mark, self.pos - mark)
    
    def expect(self, fn):
        if self.pos >= len(self.tokens):
            return False
        
        if fn(self.tokens[self.pos]):
            self.pos += 1
            return self.tokens[self.pos - 1]
        
        return None
    
    def expectIdent(self, ident = None):
        if ident and not type(ident) is list:
            ident = [ident]
        return self.expect(lambda tok: type(tok) is IdentToken and (ident == None or tok.ident in ident))
    
    def expectOp(self, op = None):
        if op and not type(op) is list:
            op = [op]
        return self.expect(lambda tok: type(tok) is OpToken and (op == None or tok.op in op))
    
    def expectNum(self, num = None):
        if num and not type(num) is list:
            num = [num]
        return self.expect(lambda tok: type(tok) is NumberToken and (num == None or tok.num in num))
    
    def expectEof(self):
        return self.expect(lambda tok: type(tok) is EofToken)
