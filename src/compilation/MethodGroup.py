

class MethodGroup(object):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.overloads = []
    
    def registerOverload(self, params, rett, impl):
        overload = { 'args': params, 'impl': impl, 'rett': rett }
        self.overloads.append(overload)
        return overload
