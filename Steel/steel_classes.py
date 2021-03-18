class Steel:
    """
    Steel 

    E_(MPa)
    fyk_(Mpa)

    """
    def __init__(self, fyk, coefmin = 1.1, E = 200000, G = 78850):
        self.E_ = E
        self.G_ = G
        self.fyk_ = fyk
        self.fyd_ = fyk / coefmin

if __name__ == '__main__':
    s = Steel(250)

    print(s.E_)
    print(s.fyd_)
