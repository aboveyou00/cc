from tokenizer import Tokenizer
from sys import argv

def main(args):
    tokenizer = Tokenizer()
    print(tokenizer.tokenize(r' 1 + 2   - 3 / (4 *7) % 32 '))
    input()

if __name__ == '__main__':
    main(argv)
