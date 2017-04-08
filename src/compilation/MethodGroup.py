

class MethodGroup(object):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.overloads = []
    
    def registerOverload(self, params, rett, impl):
        overload = { 'args': params, 'impl': impl, 'rett': rett }
        self.overloads.append(overload)
        return overload
    
    def registerFnOverload(self, fn):
        self.overloads.append(fn.overload)
    
    def findOverload(self, args):
        for overload in self.overloads:
            if overload['args'] == args:
                return overload
        return None
    
    def findPossibleOverloads(self, args):
        return [
            overload
            for overload in self.overloads
            if self.isPossibleOverload(overload, args)
        ]
    
    def isPossibleOverload(self, overload, args):
        oargs = overload['args']
        if len(oargs) != len(args):
            return False
        return all(map(self.canBeArg, zip(args, oargs)))
    
    def canBeArg(self, argPair):
        arg, oarg = argPair
        return not arg or not oarg or arg == oarg
    
    def findOverloadsByReturnType(self, rett):
        return [
            overload
            for overload in self.overloads
            if overload['rett'] == rett
        ]
