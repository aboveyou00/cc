from syntax.TreeMarker import *
from syntax.ExprSyntax import *
from syntax.ErrorSyntax import *
from syntax.AddExprSyntax import *
from syntax.MultExprSyntax import *
from syntax.TermExprSyntax import *

class SyntaxTreeParser(object):
    def __init__(self):
        super().__init__()
    
    def parseCompilationUnit(self, cunit):
        collect = TreeMarker(cunit)
        exprs = []
        
        while True:
            if collect.expectEof():
                break
            
            expr = self.parseExprSyntax(collect)
            if not expr:
                start = collect.mark()
                collect.reset(len(cunit.tokens))
                exprs.append(ErrorSyntax(*collect.argsFrom(start)))
                break
            
            exprs.append(expr)
        
        return exprs
    
    def parseExprSyntax(self, collect):
        return self.parseAddExprSyntax(collect)
    
    def parseAddExprSyntax(self, collect):
        begin = collect.mark()
        lhs = self.parseMultExprSyntax(collect)
        if not lhs:
            return None
        
        while True:
            mark = collect.mark()
            op = collect.expectOp(['+', '-'])
            if not op:
                break
            
            rhs = self.parseMultExprSyntax(collect)
            if not rhs:
                collect.reset(mark)
                break
            lhs = AddExprSyntax(*collect.argsFrom(begin), lhs, op.op, rhs)
        
        return lhs
    
    def parseMultExprSyntax(self, collect):
        begin = collect.mark()
        lhs = self.parseTermExprSyntax(collect)
        if not lhs:
            return None
        
        while True:
            mark = collect.mark()
            op = collect.expectOp(['*', '/', '%'])
            if not op:
                break
            
            rhs = self.parseTermExprSyntax(collect)
            if not rhs:
                collect.reset(mark)
                break
            lhs = MultExprSyntax(*collect.argsFrom(begin), lhs, op.op, rhs)
        
        return lhs
    
    def parseTermExprSyntax(self, collect):
        begin = collect.mark()
        if collect.expectOp('('):
            expr = self.parseExprSyntax(collect)
            if expr and collect.expectOp(')'):
                return expr
            
            collect.reset(begin)
            return None
        
        num = collect.expectNum()
        if not num:
            return None
        
        return TermExprSyntax(*collect.argsFrom(begin), num.num)
