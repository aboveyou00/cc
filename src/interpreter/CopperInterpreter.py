from emit.MethodBuilder import *

class CopperInterpreter(object):
    def __init__(self):
        super().__init__()
        self.methods = {}
        self.stackFrames = [{
            'stack': [],
            'ret': 0
        }]
    
    def eval(self, entry, args):
        assert(entry)
        args = args or []
        
        for arg in args:
            self.stackFrames[0]['stack'].append(arg)
        
        self.callMethod(entry)
        return self.stackFrames[0]['ret']
    
    def callMethod(self, method):
        methodIl = self.getAssembledMethod(method)
        
        pass
    
    def getAssembledMethod(self, method):
        if not method or not type(method) == dict:
            return None
        if not 'il' in method:
            self.assembleMethod(method)
        return method['il']
    
    def assembleMethod(self, method):
        mbuilder = MethodBuilder(method['name'] if 'name' in method else '???', len(method['args']))
        method['il'] = mbuilder
        builder = method['builder']
        assert(builder)
        
        builder.assemble(mbuilder)
        mbuilder.finalize()
        print(mbuilder)
