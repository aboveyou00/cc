from syntax.DeclSyntax import *

class FuncDeclSyntax(DeclSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, name, params, exprs):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.name = name
        self.params = params
        self.exprs = exprs
        self.mydeclspace = None
        self.fnT = self.params.createFunctionT()
    
    def registerNames(self, declspace):
        declspace.register(self.name, self)
        self.mydeclspace = declspace.fork()
        self.params.registerNames(self.mydeclspace)
        for expr in self.exprs:
            expr.registerNames(self.mydeclspace)
    
    def resolveNames(self):
        self.params.resolveNames()
        for expr in self.exprs:
            expr.resolveNames()
    
    def tryResolveTypes(self):
        changed = any([expr.tryResolveType() for expr in self.exprs])
        
        lastExpr = self.exprs[len(self.exprs) - 1]
        suggestedT = lastExpr.resolvedType()
        if suggestedT:
            changed = self.fnT.suggestReturnType(suggestedT) or changed
        
        return changed
    
    def tryResolveType(self):
        return False
    
    def resolvedType(self):
        return self.fnT
    
    def stringifyExpr(self, expr):
        exprStr = str(expr)
        spaces = ' ' * max(0, 40-len(exprStr))
        return exprStr + spaces + ' // ' + str(expr.resolvedType() or '???')
    
    def __str__(self):
        sig = 'def ' + self.name + '(' + str(self.params) + ')'
        retT = self.resolvedType().getReturnType() or '???'
        sig += ': ' + str(retT)
        if len(self.exprs) == 1:
            return sig + ' = ' + str(self.exprs[0])
        return sig + '\n  ' + '\n  '.join(map(self.stringifyExpr, self.exprs)) + '\nend'
