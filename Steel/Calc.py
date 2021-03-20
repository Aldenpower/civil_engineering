from profile_classes import ProfileWLaminated
from steel_classes import Steel
from buckling_classes import Buckling
from Anexo_E_NBR_8800 import AxialElasticBucklingForce
from math import pi

# OBJECTS
steel = Steel(250)

perfil = ProfileWLaminated(
    name = 'W150x13',
    weight = 13,
    d = 148,
    bf = 100,
    tw = 4.3,
    tf = 4.9,
    h = 138,
    d_linha = 118,
    ag = 16.6,
    ix = 635,
    wx = 85.8,
    rx = 6.2,
    zx = 96.4,
    iy = 82,
    wy = 16.4,
    ry = 2.2,
    zy = 25.5,
    rt = 2.6,
    it = 1.7,
    cw = 4181
)

buckl = Buckling(
    kx = 1,
    lx = 400,
    ky = 1,
    ly = 400,
    kz = 1,
    lz = 400
)

kxlx = buckl.kxlx_
kyly = buckl.kyly_
kzlz = buckl.kzlz_

if __name__ == '__main__':

    print('E.1.1 - Seções com dupla sim. ou simétricas em rel. a um ponto')
    
    Pcr = AxialElasticBucklingForce(
        E = steel.E_,
        G = steel.G_,
        Cw = perfil.cw_,
        It = perfil.it_,
        Ix = perfil.ix_,
        Kxlx = kxlx,
        Kyly = kyly,
        Kzlz = kzlz
    )

    print(Pcr.Nex())