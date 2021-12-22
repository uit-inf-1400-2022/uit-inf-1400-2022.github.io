import random

class KometFragment(object):
    def __init__(self):
        self.posisjon = None
        self.storrelse = None

class Komet(object):
    def __init__(self):
        self.fragmenter = [KometFragment()]

class Operasjon(object):
    def __init__(self):
        self.romskip = [SensorRomskip() for x in range(4)] + [SkyveRomskip() for x in range(4)]

    def plasserSensorRomskip(self, posisjoner):
        sensor_skip = [skip for skip in self.romskip if isinstance(skip, SensorRomskip)]
        for (romskip, ny_pos) in zip(sensor_skip, posisjoner):
            romskip.settMaalPosisjon(ny_pos)

    def __repr__(self):
        return "Operasjon!\n\t"+"\n\t".join([str(skip) for skip in self.romskip])

class Romskip(object):
    def __init__(self):
        self.posisjon = None
        self.maal_posisjon = None

    def __repr__(self):
        return self.__class__.__name__+"({0}->{1})".format(self.posisjon, self.maal_posisjon)

    def settMaalPosisjon(self, ny_maal_posisjon):
        self.maal_posisjon = ny_maal_posisjon


class SensorRomskip(Romskip):
    def __init__(self):
        Romskip.__init__(self)

class SkyveRomskip(Romskip):
    def __init__(self):
        Romskip.__init__(self)
        self.fragment = None

    def settMalPosisjon(self, ny_maal_posisjon):
        Romskip.settMalPosisjon(self, ny_maal_posisjon)
        self.fragment = None

if __name__ == "__main__":
    O = Operasjon()
    print O

    O.plasserSensorRomskip([random.randint(1,20) for x in range(4)])
    print O
