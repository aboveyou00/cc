from syntax.TreeMarker import *

from syntax.ErrorSyntax import *

from syntax.DeclSyntax import *
from syntax.FuncDeclSyntax import *

from syntax.ExprSyntax import *
from syntax.AddExprSyntax import *
from syntax.MultExprSyntax import *
from syntax.TermExprSyntax import *

class SyntaxTreeParser(object):
    def __init__(self):
        super().__init__()
    
    def parseCompilationUnit(self, cunit):
        collect = TreeMarker(cunit)
        decls = []
        
        while True:
            if collect.expectEof():
                break
            
            decl = self.parseDeclSyntax(collect)
            if not decl:
                start = collect.mark()
                collect.reset(len(cunit.tokens))
                decls.append(ErrorSyntax(*collect.argsFrom(start)))
                break
            
            decls.append(decl)
        
        return decls
    
    def parseDeclSyntax(self, collect):
        return self.parseFuncDeclSyntax(collect)
    
    def parseFuncDeclSyntax(self, collect):
        begin = collect.mark()
        
        if not collect.expectIdent('def'):
            return None
        
        name = collect.expectIdent()
        #TODO: expect parameter list
        if name and collect.expectOp('(') and collect.expectOp(')'):
            exprs = self.parseExpressionList(collect)
            if collect.expectIdent('end'):
                return FuncDeclSyntax(*collect.argsFrom(begin), name.ident, exprs)
        
        collect.reset(begin)
        return None
    
    def parseExpressionList(self, collect):
        exprs = []
        
        while True:
            expr = self.parseExprSyntax(collect)
            if not expr:
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
