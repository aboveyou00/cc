from tokenizer.Tokenizer import *
from syntax.SyntaxTreeParser import *

class CompilationUnit(object):
    def __init__(self, name, source):
        super().__init__()
        self.name = name
        self.source = source
        self.tokens = []
        self.syntax = []
    
    def tokenize(self):
        tokenizer = Tokenizer()
        self.tokens = tokenizer.tokenize(self.source)
    
    def parseSyntaxTree(self):
        parser = SyntaxTreeParser()
        self.syntax = parser.parseCompilationUnit(self)
    
    def registerNames(self, declspace):
        for syntax in self.syntax:
            syntax.registerNames(declspace)
    
    def resolveNames(self):
        for syntax in self.syntax:
            syntax.resolveNames()
    
    def tryResolveTypes(self):
        while True:
            changed = any([syntax.tryResolveTypes() for syntax in self.syntax])
            if not changed:
                break
    
    def __str__(self):
        assert(type(self.name) == str)
        assert(type(str(self.tokens)) == str)
        assert(type(str(self.syntax[0])) == str)
        return "CompilationUnit: " + self.name + "\n\nTokens: " + str(self.tokens) + "\n\nSyntax: [\n" + "\n".join(map(str, self.syntax)) + "\n]"
