from tokenizer.IdentToken import *
from tokenizer.KeywordToken import *
from tokenizer.OpToken import *
from tokenizer.ErrorToken import *
from tokenizer.EofToken import *
from tokenizer.NumberToken import *
from tokenizer.Util import isKeyword

class Tokenizer(object):
    def __init__(self):
        super().__init__()
    
    def tokenize(self, string):
        self.string = string + '\0'
        self.line_num = 0
        self.line_begin_idx = 0
        
        tokens = []
        pos = 0
        while True:
            tok, pos = self.collect_token(pos)
            if tok is None:
                break
            tokens.append(tok)
        
        tokens.append(EofToken(self.line_num, pos - self.line_begin_idx, ''))
        return tokens
    
    def collect_token(self, pos):
        pos = self.collect_ws(pos)
        
        tok_start_idx = pos - self.line_begin_idx
        
        for fn in [self.collect_ident, self.collect_op, self.collect_num, self.collect_err]:
            tok, newPos = fn(pos, tok_start_idx)
            if not tok is None:
                return (tok, newPos)
        
        return (None, newPos)
    
    def collect_ws(self, pos):
        posArr = [pos]
        while True:
            if self.string[posArr[0]] in ' \t':
                posArr[0] += 1
            elif not self.collect_nl(posArr):
                break
        
        return posArr[0]
    
    def collect_nl(self, pos):
        if self.string[pos[0]] in '\r\n':
            if (self.string[pos[0]] == '\r' and self.string[pos[0] + 1] == '\n'):
                pos[0] += 2
            else:
                pos[0] += 1
            self.line_begin_idx = pos[0]
            self.line_num += 1
            return True
        return False
    
    def collect_ident(self, pos, line_idx):
        if self.string[pos].isalpha() or self.string[pos] in '_$@':
            ident = self.string[pos]
            pos += 1
            
            while self.string[pos].isalnum() or self.string[pos] in '_$':
                ident += self.string[pos]
                pos += 1
            
            if isKeyword(ident):
                return (KeywordToken(self.line_num, line_idx, ident), pos)
            
            return (IdentToken(self.line_num, line_idx, ident), pos)
        
        return (None, pos)
    
    def collect_num(self, pos, line_idx):
        if self.string[pos].isdigit():
            numStr = self.string[pos]
            pos += 1
            
            while self.string[pos].isdigit():
                numStr += self.string[pos]
                pos += 1
            
            return (NumberToken(self.line_num, line_idx, numStr), pos)
        
        return (None, pos)
    
    def collect_op(self, pos, line_idx):
        chr = self.string[pos]
        if chr in '+-*/%(),:':
            pos += 1
            return (OpToken(self.line_num, line_idx, chr), pos)
        
        return (None, pos)
    
    def collect_err(self, pos, line_idx):
        err = ''
        
        while not self.string[pos] in '\r\n\0 \t':
            err += self.string[pos]
            pos += 1
        
        if err:
            return (ErrorToken(self.line_num, line_idx, err), pos)
        
        return (None, pos)
