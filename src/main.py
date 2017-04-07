from compilation import Compiler
from sys import argv

test_file = '''

//
// This is a comment!
//

def add(lhs, rhs) = lhs + rhs
def sub(lhs, rhs) = lhs - rhs
def mul(lhs, rhs) = lhs * rhs
def div(lhs, rhs) = lhs / rhs
def mod(lhs, rhs) = lhs % rhs

def main()
    -3
    +-+-+-42
    add(1, 1)
    mul(1, sub(5, 3))
    mod(6, 4) + div(8, 4) + +3
end

'''

def main(args):
    cc = Compiler()
    cc.addCompilationUnit('test', test_file)
    cc.compile()
    print(cc)
    input()

if __name__ == '__main__':
    main(argv)
