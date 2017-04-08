from compilation.DeclarationSpace import *

class Type(object):
    def __init__(self):
        super().__init__()
        self.declspace = DeclarationSpace()
    
    def registerOverload(self, name, params, rett, impl):
        return self.declspace.registerOverload(name, params, rett, impl)
