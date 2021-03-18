class Steel:
    """
    Steel 

    E_(MPa)
    fyk_(Mpa)

    """
    def __init__(self, fyk, coefmin = 1.1, E = 200000):
        self.E_ = E
        self.fyk_ = fyk
        self.fyd_ = fyk / coefmin

if __name__ == '__main__':
    s = Steel(250)

    print(s.E_)
    print(s.fyd_)
