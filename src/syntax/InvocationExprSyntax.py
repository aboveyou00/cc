from syntax.PrimaryExprSyntax import *

class InvocationExprSyntax(PrimaryExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, lhs, args):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.lhs = lhs
        self.args = args
    
    def registerNames(self, declspace):
        self.lhs.registerNames(declspace)
        for arg in self.args:
            arg.registerNames(declspace)
    
    def resolveNames(self):
        self.lhs.resolveNames()
        for arg in self.args:
            arg.resolveNames()
    
    def tryResolveType(self):
        if self.resolvedType():
            return False
        
        changed = self.lhs.tryResolveType() or any([arg.tryResolveType() for arg in self.args])
        leftT = self.lhs.resolvedType()
        argTs = [arg.resolvedType() for arg in self.args]
        if not leftT:
            return changed
        
        hasAllArgTypes = not any([not argT for argT in argTs])
        hasAllParamTypes = not any([not argT for argT in leftT.getArgumentTypes()])
        if not hasAllArgTypes and not hasAllParamTypes:
            return changed
        
        if not hasAllParamTypes:
            changed = leftT.suggestParamTypes(argTs) or changed
        
        if not hasAllArgTypes:
            changed = any([arg.suggestType(paramT) for arg, paramT in zip(self.args, leftT.getArgumentTypes())])
        
        print('Trying to resolve ' + str(self.lhs) + ' invoked with (' + ', '.join(map(str, argTs)) + ')')
        
        fnRetType = leftT.getReturnType()
        if fnRetType:
            self._resolvedType = fnRetType
            return True
        
        return changed
    
    def __str__(self):
        return str(self.lhs) + '(' + ', '.join(map(str, self.args)) + ')'
