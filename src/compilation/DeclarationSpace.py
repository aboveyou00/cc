from compilation.MethodGroup import *

class DeclarationSpace(object):
    def __init__(self, parent = None):
        super().__init__()
        self.parent = parent
        self.names = {}
    
    def register(self, name, handler):
        assert(not name in self.names or self.names[name] is handler)
        self.names[name] = handler
    
    def registerOverload(self, name, args, rett, impl):
        mgroup = self.resolve(name, True)
        if mgroup and not type(mgroup) == MethodGroup:
            assert(False)
        elif not mgroup:
            mgroup = MethodGroup(name)
            self.register(name, mgroup)
        
        return mgroup.registerOverload(args, rett, impl)
    
    def resolve(self, name, local = False):
        if name in self.names:
            return self.names[name]
        
        if not local and self.parent:
            return self.parent.resolve(name)
        return None
    
    def fork(self):
        return DeclarationSpace(self)
    
    def findOverload(self, name, args):
        mgroup = self.resolve(name, True)
        if not mgroup or not type(mgroup) == MethodGroup:
            return None
        
        for overload in mgroup.overloads:
            if overload['args'] == args:
                return overload
        return None
    
    def findOverloadsByReturnType(self, name, rett):
        mgroup = self.resolve(name, True)
        if not mgroup or not type(mgroup) == MethodGroup:
            return None
        
        return [overload for overload in mgroup.overloads if overload['rett'] == rett]
