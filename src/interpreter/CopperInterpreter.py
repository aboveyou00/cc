from emit.MethodBuilder import *

class CopperInterpreter(object):
    def __init__(self):
        super().__init__()
        self.methods = {}
        self.stackFrames = []
    
    def eval(self, entry, args):
        assert(entry)
        args = args or []
        
        stackFrame = {
            'stack': [arg for arg in args]
        }
        self.stackFrames.append(stackFrame)
        self.callMethod(entry)
        ret = self.stackFrames[0]['stack'][0]
        self.stackFrames.clear()
        return ret
    
    def callMethod(self, method):
        methodIl = self.getAssembledMethod(method)
        prevStackFrame = self.stackFrames[-1]
        
        prevStack = prevStackFrame['stack']
        assert(len(prevStack) >= methodIl.argc)
        splitIdx = len(prevStack) - methodIl.argc
        args = prevStack[splitIdx:]
        prevStack = prevStackFrame['stack'] = prevStack[:splitIdx]
        
        stackFrame = {
            'stack': [],
            'locals': args
        }
        self.stackFrames.append(stackFrame)
        
        self.interpretIl(methodIl)
        assert(len(stackFrame['stack']) == 1)
        prevStack.append(stackFrame['stack'][0])
        self.stackFrames.pop()
    
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
        mbuilder.optimize()
        mbuilder.finalize()
        print(mbuilder)
    
    def interpretIl(self, methodIl):
        ip = 0
        opcodes = methodIl.opcodes
        stackFrame = self.stackFrames[-1]
        stack = stackFrame['stack']
        locals = stackFrame['locals']
        
        while ip < len(opcodes):
            op = opcodes[ip]
            
            if op == 'nop':
                ip += 1
            
            elif op == 'pop':
                stack.pop()
                ip += 1
            
            elif op == 'neg':
                stack.append(-stack.pop())
                ip += 1
            
            elif op == 'add':
                stack.append(stack.pop(-2) + stack.pop())
                ip += 1
            
            elif op == 'sub':
                stack.append(stack.pop(-2) - stack.pop())
                ip += 1
            
            elif op == 'mul':
                stack.append(stack.pop(-2) * stack.pop())
                ip += 1
            
            elif op == 'div':
                stack.append(stack.pop(-2) / stack.pop())
                ip += 1
            
            elif op == 'mod':
                stack.append(stack.pop(-2) % stack.pop())
                ip += 1
            
            elif type(op) == tuple:
                opn = op[0]
                
                if opn == 'ldc':
                    stack.append(op[1])
                    ip += 1
                
                elif opn == 'call':
                    self.callMethod(op[1])
                    stack = stackFrame['stack']
                    ip += 1
                
                elif opn == 'ldloc':
                    stack.append(locals[op[1]])
                    ip += 1
                
                else:
                    assert(False)
            
            else:
                assert(False)
