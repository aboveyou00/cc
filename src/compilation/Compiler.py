from compilation.CompilationUnit import *
from compilation.DeclarationSpace import *
from interpreter.CopperInterpreter import *

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
        
        interpreter = CopperInterpreter()
        main = self.resolveMain()
        if not main:
            print('ERROR: Failed to find entrypoint.')
            return
        
        result = interpreter.eval(main, [])
        print('result: ' + str(result))
    
    def resolveMain(self):
        return self.declspace.findOverload('main', [])
    
    def __str__(self):
        return 'Compiler (' + str(len(self.cunits)) + ' compilation units):\n\n' + '\n\n'.join(map(str, self.cunits))
