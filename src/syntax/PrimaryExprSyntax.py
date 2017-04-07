from syntax.Syntax import *
from syntax.TermExprSyntax import *
from syntax.Util import isSubclassOfAny

class PrimaryExprSyntax(Syntax):
    def __init__(self, cunit, tok_start_idx, tok_count):
        super().__init__(cunit, tok_start_idx, tok_count)
    
    def isHigherPrecedence(self, other):
        return isSubclassOfAny(other, [TermExprSyntax])
