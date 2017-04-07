from syntax.Syntax import *

class ErrorSyntax(Syntax):
    def __init__(self, cunit, tok_start_idx, tok_count):
        super().__init__(cunit, tok_start_idx, tok_count)
    
    def __str__(self):
        return 'ERROR(' + super().__str__() + ')'
