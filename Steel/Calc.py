from profile_classes import ProfileWLaminated
from steel_classes import Steel
from buckling_classes import Buckling
from Anexo_E_NBR_8800 import AxialElasticBucklingForce
from math import pi
import pandas as pd

# PROFILE LOADING
profilewlaminated = pd.read_csv('ProfileWLaminated.csv')

# OBJECTS

    # STEEL
steel = Steel(250)

    # PROFILE
profile_number = 0

perfil = ProfileWLaminated(
    name = profilewlaminated['name'].iloc[profile_number],
    weight = profilewlaminated['weight'].iloc[profile_number],
    d = profilewlaminated['d'].iloc[profile_number],
    bf = profilewlaminated['bf'].iloc[profile_number],
    tw = profilewlaminated['tw'].iloc[profile_number],
    tf = profilewlaminated['tf'].iloc[profile_number],
    h = profilewlaminated['h'].iloc[profile_number],
    d_linha = profilewlaminated['d_linha'].iloc[profile_number],
    ag = profilewlaminated['ag'].iloc[profile_number],
    ix = profilewlaminated['ix'].iloc[profile_number],
    wx = profilewlaminated['wx'].iloc[profile_number],
    rx = profilewlaminated['rx'].iloc[profile_number],
    zx = profilewlaminated['zx'].iloc[profile_number],
    iy = profilewlaminated['iy'].iloc[profile_number],
    wy = profilewlaminated['wy'].iloc[profile_number],
    ry = profilewlaminated['ry'].iloc[profile_number],
    zy = profilewlaminated['zy'].iloc[profile_number],
    rt = profilewlaminated['rt'].iloc[profile_number],
    it = profilewlaminated['it'].iloc[profile_number],
    cw = profilewlaminated['Cw'].iloc[profile_number]
)
    # BUCKLING
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