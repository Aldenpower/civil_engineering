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
    lx = 500,
    ky = 1,
    ly = 500,
    kz = 1,
    lz = 400
)


if __name__ == '__main__':

    print('E.1.1 - Seções com dupla sim. ou simétricas em rel. a um ponto')
    
    Pcr = AxialElasticBucklingForce(
        steel,
        perfil,
        buckl,
        case = 'E.1.1'
    )

    print(Pcr.Nex())
    print(Pcr.Ney())
    print(Pcr.Nez())