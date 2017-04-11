from stdtypes.Type import *
from stdtypes.Util import *

class Function(Type):
    def __init__(self, name, args, rett):
        super().__init__()
        self.name = name
        self.registerMethods(args, rett)
    
    def registerMethods(self, args, rett):
        self.overload = self.registerOverload(OP_CALL, args, rett, self.emitCall)
        self.overload['name'] = self.name
    
    def getArgumentTypes(self):
        return self.overload['args']
    
    def getReturnType(self):
        return self.overload['rett']
    
    def emitCall(self, builder):
        builder.emit(('call', self))
    
    def __str__(self):
        args = ', '.join(map(lambda at: str(at) if at else '???', self.getArgumentTypes()))
        rett = str(self.getReturnType()) if self.getReturnType() else '???'
        return 'def ' + self.name + '(' + args + '):' + rett
