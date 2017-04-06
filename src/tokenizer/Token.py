

class Token(object):
    def __init__(self, linen, start, orig):
        super().__init__()
        self.linen = linen
        self.start = start
        self.orig = orig
    
    def __str__(self):
        return self.orig
    
    def __repr__(self):
        return str(self)
