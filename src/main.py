from compilation import Compiler
from sys import argv

test_file = '''

// This is a comment!
//add(1, 1)
//sub(5, 3)
//mul(1, 2)
//div(8, 4)
//mod(6, 4)
//

def add(lhs, rhs)
    lhs + rhs
end

def sub(lhs, rhs)
    lhs - rhs
end

def mul(lhs, rhs)
    lhs * rhs
end

def div(lhs, rhs)
    lhs / rhs
end

def mod(lhs, rhs)
    lhs % rhs
end

def main()
    1+2+3
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
