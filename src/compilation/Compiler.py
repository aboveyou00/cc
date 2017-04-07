from compilation.CompilationUnit import *

class Compiler(object):
    def __init__(self):
        super().__init__()
        self.cunits = []
        self.finalized = False
    
    def addCompilationUnit(self, name, source):
        assert(not self.finalized)
        cunit = CompilationUnit(name, source)
        self.cunits.append(cunit)
    
    def compile(self):
        assert(not self.finalized)
        self.finalized = True
        
        for cunit in self.cunits:
            cunit.tokenize()
        
        for cunit in self.cunits:
            cunit.parseSyntaxTree()
    
    def __str__(self):
        return 'Compiler (' + str(len(self.cunits)) + ' compilation units):\n\n' + '\n\n'.join(map(str, self.cunits))
