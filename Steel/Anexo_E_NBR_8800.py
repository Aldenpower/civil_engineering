from math import pi

class AxialElasticBucklingForce:

    def __init__(self, steel, profile, buckling, case):
        self.steel_ = steel
        self.profile_ = profile
        self.buckling_ = buckling
        self.case_ = case
    def Nex(self, report = False):
        if self.case_ == 'E.1.1':
            Nex = ((pi ** 2) * (self.steel_.E_ * 0.1) * self.profile_.ix_ /
            ((self.buckling_.kxlx_) ** 2))

            if report:
                buckling_reason = self.buckling_.kxlx_ / self.profile_.rx_

                #kN/cm2
                tension = ((pi ** 2) * (self.steel_.E_ * 0.1) /
                (buckling_reason ** 2))

                print('Nex', round(Nex, 2), 'Buckling reason', round(buckling_reason, 2),
                'Tension', round(tension, 2), sep = '\n')

            #kN
            return round(Nex, 2)

    
    def Ney(self, report = False):
        if self.case_ == 'E.1.1':
            Ney = ((pi ** 2) * (self.steel_.E_ * 0.1) * self.profile_.iy_ /
            ((self.buckling_.kyly_) ** 2))

            if report:
                buckling_reason = self.buckling_.kyly_ / self.profile_.ry_

                tension = ((pi ** 2) * (self.steel_.E_ * 0.1) /
                (buckling_reason ** 2))

                print('Ney', round(Ney, 2), 'Buckling reason', round(buckling_reason, 2),
                'Tension', round(tension, 2), sep = '\n')

            #kN
            return round(Ney, 2)

    def Nez(self, report = False):
        if self.case_ == 'E.1.1':
            ro = (((self.profile_.rx_) ** 2) + ((self.profile_.ry_) ** 2)) ** 0.5

            Nez = (1 / (ro ** 2)) * (((pi ** 2) * self.steel_.E_ * 0.1 *
            self.profile_.cw_) / ((self.buckling_.kzlz_) ** 2) + 
            (self.steel_.G_ * self.profile_.it_))

            if report:
                buckling_reason = self.buckling_.kzlz_ / self.profile_.rt_

                tension = ((pi ** 2) * (self.steel_.E_ * 0.1) /
                (buckling_reason ** 2))

                print('Nez', round(Nez, 2), 'Buckling reason', round(buckling_reason, 2),
                'Tension', round(tension, 2), sep = '\n')
            #kN
            return round(Nez, 2)
