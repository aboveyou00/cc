from stdtypes.Type import *
from stdtypes.Util import *

class Int(Type):
    def __init__(self):
        super().__init__()
        if Int._inst:
            raise Exception('Use inst() to get an instance, instead of creating a new one!')
        Int._inst = self
        self.registerMethods()
    
    _inst = None
    def inst():
        return Int._inst or Int()
    
    def registerMethods(self):
        self.registerOverload(OP_UN_PLUS, [self], self, self.emitUnPlus)
        self.registerOverload(OP_UN_NEG, [self], self, self.emitNegate)
        
        self.registerOverload(OP_ADD, [self, self], self, self.emitAdd)
        self.registerOverload(OP_SUB, [self, self], self, self.emitSub)
        self.registerOverload(OP_MUL, [self, self], self, self.emitMul)
        self.registerOverload(OP_DIV, [self, self], self, self.emitDiv)
        self.registerOverload(OP_MOD, [self, self], self, self.emitMod)
    
    def emitUnPlus(self, builder):
        builder.emit(('nop'))
    
    def emitNegate(self, builder):
        builder.emit(('neg'))
    
    def emitAdd(self, builder):
        builder.emit(('add'))
    
    def emitSub(self, builder):
        builder.emit(('sub'))
    
    def emitMul(self, builder):
        builder.emit(('mul'))
    
    def emitDiv(self, builder):
        builder.emit(('div'))
    
    def emitMod(self, builder):
        builder.emit(('mod'))
    
    def __str__(self):
        return 'int'
