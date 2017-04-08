from syntax.BinaryExprSyntax import *
from syntax.MultExprSyntax import *
from syntax.UnaryExprSyntax import *
from syntax.PrimaryExprSyntax import *
from syntax.TermExprSyntax import *
from syntax.Util import isSubclassOfAny
from stdtypes.Util import OP_ADD, OP_SUB

class AddExprSyntax(BinaryExprSyntax):
    def __init__(self, cunit, tok_start_idx, tok_count, lhs, op, rhs):
        super().__init__(cunit, tok_start_idx, tok_count, lhs, op, rhs)
    
    opMap = { '+': OP_ADD, '-': OP_SUB }
    
    def isHigherPrecedence(self, other):
        return isSubclassOfAny(other, [MultExprSyntax, UnaryExprSyntax, PrimaryExprSyntax, TermExprSyntax])
