class pion:
    def __init__(self):
        self.re = None
        self.ro = None
        self.fo = None
        self.ca = None
        self.to = None
        self.pi = None

class texture:
    def __init__(self):
        self.board = None
        self.greenpace = None
        self.orange = None
        self.redpace = None
        self.white = pion()
        self.black = pion()

class info:
    def __init__(self):
        self.board = None
        self.board2 = None
        self.fenetre = None
        self.text = texture()
        self.xp = 0
        self.yp = 0