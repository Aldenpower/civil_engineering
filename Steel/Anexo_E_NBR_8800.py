from math import pi

class AxialElasticBucklingForce:

    def __init__(self, steel, profile, buckling, case):
        self.steel_ = steel
        self.profile_ = profile
        self.buckling_ = buckling
        self.case_ = case
    def Nex(self):
        if self.case_ == 'E.1.1':
            Nex = ((pi ** 2) * (self.steel_.E_ * 0.1) * self.profile_.ix_ /
            ((self.buckling_.kxlx_) ** 2))

            return Nex
    
    def Ney(self):
        if self.case_ == 'E.1.1':
            Ney = ((pi ** 2) * (self.steel_.E_ * 0.1) * self.profile_.iy_ /
            ((self.buckling_.kyly_) ** 2))

            return Ney

    def Nez(self):
        if self.case_ == 'E.1.1':
            ro = (((self.profile_.rx_) ** 2) + ((self.profile_.ry_) ** 2)) ** 0.5
            print(ro)