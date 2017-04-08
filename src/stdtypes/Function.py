from stdtypes.Type import *
from stdtypes.Util import *

class Function(Type):
    def __init__(self, argc):
        super().__init__()
        self.registerMethods(argc)
    
    def registerMethods(self, argc):
        self.overload = self.registerOverload(OP_CALL, [None for n in range(argc)], None, self.emitCall)
    
    def getArgumentTypes(self):
        return self.overload['args']
    
    def getReturnType(self):
        return self.overload['rett']
    
    def suggestParamTypes(self, suggestedTypes):
        paramTypes = self.getArgumentTypes()
        if len(paramTypes) != len(suggestedTypes):
            assert(False)
        
        changed = False
        for paramIdx in range(len(suggestedTypes)):
            param = paramTypes[paramIdx]
            suggestedT = suggestedTypes[paramIdx]
            if not param:
                paramTypes[paramIdx] = suggestedT
                changed = True
            
            elif param != suggestedT:
                assert(False)
        
        return changed
    
    def suggestReturnType(self, suggestedType):
        retType = self.getReturnType()
        if not retType:
            self.overload['rett'] = suggestedType
            return True
        elif retType != suggestedType:
            assert(False)
    
    def emitCall(self):
        pass
    
    def __str__(self):
        args = ', '.join(map(lambda at: str(at) if at else '???', self.getArgumentTypes()))
        rett = str(self.getReturnType()) if self.getReturnType() else '???'
        return 'def(' + args + '):' + rett
