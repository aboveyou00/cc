

class DeclarationSpace(object):
    def __init__(self, parent = None):
        super().__init__()
        self.parent = parent
        self.names = {}
    
    def register(self, name, handler):
        assert(not name in self.names)
        self.names[name] = handler
    
    def resolve(self, name, local = False):
        if name in self.names:
            return self.names[name]
        
        if not local and self.parent:
            return self.parent.resolve(name)
        return None
    
    def fork(self):
        return DeclarationSpace(self)
