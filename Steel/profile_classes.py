class ProfileWLaminated:
    """
    W Laminated profile

    name_ = String
    weight_(kg)
    d_(mm)
    bf_(mm)
    tw_(mm)
    tf_(mm)
    h_(mm)
    d_linha_(mm)
    ag_(cm2)
    ix_(cm4)
    wx_(cm3)
    rx_(cm)
    zx_(cm3)
    iy_(cm4)
    wy_(cm3)
    ry_(cm)
    zy_(cm3)
    rt_(cm)
    it_(cm4)
    cw_(cm6)

    """

    def __init__(self, name, weight, d, bf, tw, tf, h, d_linha, ag, ix, wx,
    rx, zx, iy, wy, ry, zy, rt, it, cw):
        self.name_ = name
        self.weight_ = weight
        self.d_ = d
        self.bf_ = bf
        self.tw_ = tw
        self.tf_ = tf
        self.h_ = h
        self.d_linha_ = d_linha
        self.ag_ = ag
        self.ix_ = ix
        self.wx_ = wx
        self.rx_ = rx
        self.zx_ = zx
        self.iy_ = iy
        self.wy_ = wy
        self.ry_ = ry
        self.zy_ = zy
        self.rt_ = rt
        self.it_ = it
        self.cw_ = cw


if __name__ == '__main__':
    p = ProfileWLaminated(
        'W150x13', 13, 148, 100, 4.3, 4.9, 138, 118, 16.6, 635, 85.8, 6.2,
        96.4, 82, 16.4, 2.2, 25.5, 2.6, 1.7, 4181
    )

    print(p.bf_)
