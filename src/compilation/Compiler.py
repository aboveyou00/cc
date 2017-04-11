from compilation.CompilationUnit import *
from compilation.DeclarationSpace import *

class Compiler(object):
    def __init__(self):
        super().__init__()
        self.cunits = []
        self.finalized = False
        self.declspace = DeclarationSpace()
    
    def addCompilationUnit(self, name, source):
        assert(not self.finalized)
        cunit = CompilationUnit(name, source)
        self.cunits.append(cunit)
    
    def compile(self):
        assert(not self.finalized)
        self.finalized = True
        
        steps = [
            ['tokenize'],
            ['parseSyntaxTree'],
            ['registerNames', self.declspace],
            ['resolveNames'],
            ['tryResolveTypes']
        ]
        
        for step in steps:
            for cunit in self.cunits:
                getattr(cunit, step[0])(*step[1:])
        
        return True
    
    def __str__(self):
        return 'Compiler (' + str(len(self.cunits)) + ' compilation units):\n\n' + '\n\n'.join(map(str, self.cunits))
