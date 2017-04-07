from compilation import Compiler
from sys import argv

def main(args):
    cc = Compiler()
    # cc.addCompilationUnit('test', ' 1 + 2   - 3 / (4 *7) % 32 ')
    cc.addCompilationUnit('test', '1+2-3/(4*7)%32')
    cc.compile()
    print(cc)
    input()

if __name__ == '__main__':
    main(argv)
