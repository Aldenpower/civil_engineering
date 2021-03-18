class Buckling:
    """
    Buckling

    """
    def __init__(self, kx, lx, ky, ly, kz, lz):
        self.kx_ = kx
        self.lx_ = lx
        self.ky_ = ky
        self.ly_ = ly
        self.kz_ = kz
        self.lz_ = lz
        self.kxlx_ = kx * lx
        self.kyly_ = ky * ly
        self.kzlz_ = kz * lz

if __name__ == '__main__':
    b = Buckling(
        kx = 1,
        lx = 3,
        ky = 1,
        ly = 3,
        kz = 1,
        lz = 3
    )

    print(b.kxlx_)
    print(b.kyly_)