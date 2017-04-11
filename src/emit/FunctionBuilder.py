from stdtypes.Function import *

class FunctionBuilder(Function):
    def __init__(self, name, argc, syntax):
        super().__init__(name, [None for n in range(argc)], None)
        self.overload['builder'] = self
        self.syntax = syntax
    
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
    
    def assemble(self, builder):
        self.syntax.assemble(builder)
