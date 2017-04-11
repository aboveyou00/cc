

class MethodBuilder(object):
    def __init__(self, name, argc):
        super().__init__()
        self.name = name
        self.opcodes = []
        self.argc = argc
        self.localc = 0
    
    def emit(self, opcode):
        self.opcodes.append(opcode)
    
    def stringifyOpcode(self, opcode):
        return ' '.join(map(str, opcode)) if type(opcode) == tuple else str(opcode)
    
    def optimize(self):
        #Not a ton of optimization going on here yet :)
        self.opcodes = [
            opcode
            for opcode in self.opcodes
            if not opcode == ('nop')
        ]
    
    def finalize(self):
        pass
    
    def __str__(self):
        return 'def ' + self.name + '(' + str(self.argc) + ' args, ' + str(self.localc) + ' locals):\n  ' + '\n  '.join(map(self.stringifyOpcode, self.opcodes))
