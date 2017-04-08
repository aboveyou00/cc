from syntax.Syntax import *

class DeclSyntax(Syntax):
    def __init__(self, cunit, tok_start_idx, tok_count):
        super().__init__(cunit, tok_start_idx, tok_count)
    
    def registerNames(self, declspace):
        assert(False)
    
    def resolveNames(self):
        assert(False)
    
    def tryResolveTypes(self):
        assert(False)
