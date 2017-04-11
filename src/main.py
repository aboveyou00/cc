from compilation import Compiler
from sys import argv
from interpreter.CopperInterpreter import *

test_file = '''

//
// This is a comment!
//

def test(test) = test

def add(lhs, rhs) = lhs + rhs
def sub(lhs, rhs) = lhs - rhs
def mul(lhs, rhs) = lhs * rhs
def div(lhs, rhs) = lhs / rhs
def mod(lhs, rhs) = lhs % rhs

def main()
    test(-3)
    +-+-+-42
    add(1, 1)
    mul(1, sub(5, 3))
    mod(6, 4) + div(8, 4) + +3
end

'''

def main(args):
    cc = Compiler()
    cc.addCompilationUnit('test', test_file)
    if not cc.compile():
        print('ERROR: Failed to compile.')
        return
    
    interpreter = CopperInterpreter()
    main = cc.declspace.findOverload('main', [])
    if not main:
        print('ERROR: Failed to find entrypoint.')
        return
    
    result = interpreter.eval(main, [])
    print('Result: ' + str(result))
    input()

if __name__ == '__main__':
    main(argv)
