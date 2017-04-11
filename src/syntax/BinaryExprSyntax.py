from syntax.ExprSyntax import *

class BinaryExprSyntax(ExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, lhs, op, rhs):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.lhs = lhs
        self.op = op
        self.rhs = rhs
        self.overload = None
    
    def registerNames(self, declspace):
        self.lhs.registerNames(declspace)
        self.rhs.registerNames(declspace)
    
    def resolveNames(self):
        self.lhs.resolveNames()
        self.rhs.resolveNames()
    
    def tryResolveType(self):
        if self.resolvedType():
            return False
        
        changed = self.lhs.tryResolveType() or self.rhs.tryResolveType()
        leftT = self.lhs.resolvedType()
        rightT = self.rhs.resolvedType()
        if not leftT or not rightT:
            return changed
        
        opName = self.resolveOperatorName(self.op)
        assert(opName)
        
        self.overload = leftT.declspace.findOverload(opName, [leftT, rightT])
        if not self.overload:
            return changed
        
        self._resolvedType = self.overload['rett']
        return self._resolvedType != None or changed
    
    def resolveOperatorName(self, op):
        selfT = type(self)
        ops = getattr(type(self), 'opMap', None)
        if ops:
            if op in ops:
                return ops[op]
        return None
    
    def assemble(self, builder):
        self.lhs.assemble(builder)
        self.rhs.assemble(builder)
        self.overload['impl'](builder)
    
    def __str__(self):
        return self.precendenceParens(self.lhs) + ' ' + self.op + ' ' + self.precendenceParens(self.rhs)
