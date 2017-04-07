from syntax.TreeMarker import *

from syntax.ErrorSyntax import *

from syntax.DeclSyntax import *
from syntax.FuncDeclSyntax import *
from syntax.ParamListSyntax import *
from syntax.ParamSyntax import *

from syntax.ExprSyntax import *
from syntax.AddExprSyntax import *
from syntax.MultExprSyntax import *
from syntax.UnaryExprSyntax import *
from syntax.InvocationExprSyntax import *
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
        
        if not collect.expectKeyword('def'):
            return None
        
        name = collect.expectIdent()
        if name and collect.expectOp('('):
            params = self.parseParamListSyntax(collect)
            if collect.expectOp(')'):
                exprs = self.parseExpressionList(collect)
                if collect.expectKeyword('end'):
                    return FuncDeclSyntax(*collect.argsFrom(begin), name.ident, params, exprs)
        
        collect.reset(begin)
        return None
    
    def parseParamListSyntax(self, collect):
        begin = collect.mark()
        params = []
        
        while True:
            pbegin = collect.mark()
            if len(params) > 0 and not collect.expectOp(','):
                break
            
            param = self.parseParamSyntax(collect)
            if not param:
                collect.reset(pbegin)
                break
            
            params.append(param)
        
        return ParamListSyntax(*collect.argsFrom(begin), params)
    
    def parseParamSyntax(self, collect):
        begin = collect.mark()
        
        name = collect.expectIdent()
        if not name:
            return None
        
        tbegin = collect.mark()
        if collect.expectOp(':'):
            type = self.parseTypeSyntax(collect)
            if type:
                return ParamSyntax(*collect.argsFrom(begin), name.ident, type)
            collect.reset(tbegin)
        
        return ParamSyntax(*collect.argsFrom(begin), name.ident)
    
    def parseTypeSyntax(self, collect):
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
            if not collect.expectSameLine():
                break
            
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
        lhs = self.parseUnaryExprSyntax(collect)
        if not lhs:
            return None
        
        while True:
            mark = collect.mark()
            if not collect.expectSameLine():
                break
            
            op = collect.expectOp(['*', '/', '%'])
            if not op:
                break
            
            rhs = self.parseUnaryExprSyntax(collect)
            if not rhs:
                collect.reset(mark)
                break
            lhs = MultExprSyntax(*collect.argsFrom(begin), lhs, op.op, rhs)
        
        return lhs
    
    def parseUnaryExprSyntax(self, collect):
        begin = collect.mark()
        op = collect.expectOp(['+', '-'])
        if not op:
            return self.parsePrimaryExprSyntax(collect)
        
        if not collect.expectSameLine():
            return None
        
        rhs = self.parseUnaryExprSyntax(collect)
        if not rhs:
            collect.reset(begin)
            return None
        
        return UnaryExprSyntax(*collect.argsFrom(begin), op.op, rhs)
    
    def parsePrimaryExprSyntax(self, collect):
        begin = collect.mark()
        lhs = self.parseTermExprSyntax(collect)
        if not lhs:
            return None
        
        while True:
            reset = collect.mark()
            if not collect.expectSameLine() or not collect.expectOp('('):
                break
            
            args = self.parseArgumentList(collect)
            if not collect.expectOp(')'):
                collect.reset(reset)
                break
            lhs = InvocationExprSyntax(*collect.argsFrom(begin), lhs, args)
        
        return lhs
    
    def parseArgumentList(self, collect):
        args = []
        
        while True:
            if len(args) > 0 and not collect.expectOp(','):
                break
            
            arg = self.parseExprSyntax(collect)
            if not arg:
                break
            
            args.append(arg)
        
        return args
    
    def parseTermExprSyntax(self, collect):
        begin = collect.mark()
        if collect.expectOp('('):
            expr = self.parseExprSyntax(collect)
            if expr and collect.expectOp(')'):
                return expr
            
            collect.reset(begin)
            return None
        
        num = collect.expectNum()
        if num:
            return TermExprSyntax(*collect.argsFrom(begin), num.num)
        
        ident = collect.expectIdent()
        if ident:
            return TermExprSyntax(*collect.argsFrom(begin), ident.ident)
        
        return None
