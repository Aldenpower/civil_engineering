class AxialElasticBucklingForce:

    def __init__(self, E, G, Cw, It, Ix, Kxlx, Kyly, Kzlz, case = 'E.1.1'):
        self.E_ = E
        self.G_ = G
        self.Cw_ = Cw
        self.It_ = It
        self.Ix_ = Ix
        self.Kxlx_ = Kxlx
        self.Kyly_ = Kyly
        self.Kzlz_ = Kzlz
        self.case_ = case
    
    def Nex(self):
        if self.case_ == 'E.1.1':
            Nex = ((pi ** 2) * (self.E_ * 0.1) * self.Ix_ / ((self.Kxlx_) ** 2))
            return Nex
