from syntax.ExprSyntax import *
from syntax.PrimaryExprSyntax import *
from syntax.TermExprSyntax import *
from syntax.Util import isSubclassOfAny
from stdtypes.Util import OP_UN_PLUS, OP_UN_NEG

class UnaryExprSyntax(ExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, op, operand):
        super().__init__(cunit, tok_start_idx, tok_count)
        self.op = op
        self.operand = operand
    
    opMap = { '+': OP_UN_PLUS, '-': OP_UN_NEG }
    
    def registerNames(self, declspace):
        self.operand.registerNames(declspace)
    
    def resolveNames(self):
        self.operand.resolveNames()
    
    def tryResolveType(self):
        if self.resolvedType():
            return False
        
        changed = self.operand.tryResolveType()
        operandT = self.operand.resolvedType()
        if not operandT:
            return changed
        
        opName = self.resolveOperatorName(self.op)
        assert(opName)
        print('Trying to resolve ' + opName + '(' + str(operandT) + ')')
        
        self.overload = operandT.declspace.findOverload(opName, [operandT])
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
    
    def isHigherPrecedence(self, other):
        return isSubclassOfAny(other, [PrimaryExprSyntax, TermExprSyntax])
    
    def __str__(self):
        return self.op + self.precendenceParens(self.operand)
