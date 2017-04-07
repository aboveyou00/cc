from compilation import Compiler
from sys import argv

test_file = '''

def add()
    1+2
end

def sub()
    5-3
end

def mul()
    1*2
end

def div()
    8/4
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
