from syntax.PrimaryExprSyntax import *
from stdtypes.Util import OP_CALL

class InvocationExprSyntax(PrimaryExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, lhs, args):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.lhs = lhs
        self.args = args
        self.overload = None
    
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
        
        changed = self.lhs.tryResolveType()
        changed = any([arg.tryResolveType() for arg in self.args]) or changed
        leftT = self.lhs.resolvedType()
        argTs = [arg.resolvedType() for arg in self.args]
        if not leftT:
            return changed
        
        if not self.overload:
            methodGroup = leftT if type(leftT) == MethodGroup else leftT.declspace.findMethodGroup(OP_CALL)
            overloads = methodGroup.findPossibleOverloads(argTs)
            if len(overloads) == 1:
                self.overload = overloads[0]
                changed = True
            else:
                return changed
        
        hasAllArgTypes = not any([not argT for argT in argTs])
        hasAllParamTypes = not any([not argT for argT in self.overload['args']])
        if not hasAllArgTypes and not hasAllParamTypes:
            return changed
        
        if not hasAllParamTypes:
            suggestFn = getattr(self.overload['builder'], 'suggestParamTypes', None)
            if suggestFn:
                changed = suggestFn(argTs) or changed
        
        if not hasAllArgTypes:
            changed = any([
                arg.suggestType(paramT)
                for arg, paramT in zip(self.args, self.overload['args'])
            ]) or changed
        
        fnRetType = self.overload['rett']
        if fnRetType:
            self._resolvedType = fnRetType
            return True
        
        return changed
    
    def assemble(self, builder):
        self.lhs.assemble(builder)
        for arg in self.args:
            arg.assemble(builder)
        self.overload['impl'](builder)
    
    def __str__(self):
        return str(self.lhs) + '(' + ', '.join(map(str, self.args)) + ')'
