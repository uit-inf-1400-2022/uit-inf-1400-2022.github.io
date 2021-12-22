# -*- coding: utf-8 -*-

import random

#http://stackoverflow.com/questions/456672/class-factory-in-python
class TingFactory():
    @classmethod
    def getRandomTing(self):
        return random.choice(Ting.__subclasses__()[:-1])

class Ting(object):
    def __init__(self, rom_nummer):
        self.rom_nummer = rom_nummer
        self.artikkel = "en"

    def __repr__(self):
        return "{0} {1}".format(self.artikkel, self.__class__.__name__)
    
class Pappeske(Ting):
    def __init__(self, rom_nummer):
        Ting.__init__(self, rom_nummer)
        
class Stol(Ting):
    def __init__(self, rom_nummer):
        Ting.__init__(self, rom_nummer)
        
class Bord(Ting):
    def __init__(self, rom_nummer):
        Ting.__init__(self, rom_nummer)
        self.artikkel = "et"        
        
class Rom(Ting):
    def __init__(self, rom_nummer, eiendeler = []):
        Ting.__init__(self, rom_nummer)
        self.eiendeler = eiendeler
        self.artikkel = "et"
    
    def fjern(self, ting):
        self.eiendeler.remove(ting)

    def leggTil(self, ting):
        self.eiendeler.append(ting)
    
class NTFAK():
    def __init__(self, antall_rom):
        self.rom = [Rom(nummer, [TingFactory.getRandomTing()(random.randint(0, antall_rom-1)) for x in range(random.randint(1,2))]) for nummer in range(antall_rom)]
                
        
    def finnEiendeler(self, rom_nummer):
        feil_plasserte_ting = []
        for rom in [rom for rom in self.rom if rom.rom_nummer != rom_nummer]:
            feil_plasserte_ting += [(ting, rom.rom_nummer) for ting in rom.eiendeler if ting.rom_nummer == rom_nummer]

        return feil_plasserte_ting

    def flyttEiendeler(self, rom_nummer):
        ting_som_skal_flyttes = ntfak.finnEiendeler(rom_nummer)
        for ting, fra in ting_som_skal_flyttes:
            self.rom[fra].fjern(ting)
            self.rom[ting.rom_nummer].leggTil(ting)

    #hjelpe funksjon for testing, ikke en del av eksamen
    def flyttAlleEiendeler(self):
        for rom in range(len(self.rom)):
            self.flyttEiendeler(rom)
            
    
    #hjelpe funksjon for testing, ikke en del av eksamen
    def printStatus(self):
        print "Status:"
        for rom in ntfak.rom:
            if len(rom.eiendeler) > 1:
                print "I rom {0} har vi {1} og {2}".format(rom.rom_nummer, ", ".join(["{0}({1})".format(ting, ting.rom_nummer) for ting in rom.eiendeler[:-1]]), "{0}({1})".format(rom.eiendeler[-1], rom.eiendeler[-1].rom_nummer))
            elif len(rom.eiendeler) == 1:
                print "I rom {0} har vi {1}".format(rom.rom_nummer, "{0}({1})".format(rom.eiendeler[-1], rom.eiendeler[-1].rom_nummer))

        ting_som_skal_flyttes = [ntfak.finnEiendeler(rom.rom_nummer) for rom in ntfak.rom]
        
        
        #extra credits: refaktorer denne til å bli forståelig!
        print "\n\n".join(["Ting som skal flyttes til rom {0} er \n\t{1}".format(idx, "\n\t".join(["{0} i rom {1}".format(x[0], x[1]) for x in items])) for idx, items in enumerate(ting_som_skal_flyttes) if len(items) > 0])  

        #denne løkken er ekvivalent til setningen over
        #for idx, items in enumerate(ting_som_skal_flyttes):
        #   if len(items) > 0:
        #       print "Ting som skal flyttes til rom {0} er".format(idx)
        #       print "\t","\n\t".join(["{0} i rom {1}".format(x[0], x[1]) for x in items])
        #       print       

        print


class Thing:
    def __init__(self):
        self._a = 1
        self._b = 4
        
    def foo(self, param):
        self._a = self._a + param
        self._b = self._b + param
        return (self._a + self._b)
        
    def bar(self, param):
        a = self._a + param
        b = self._b + param
        return (a + b)

    def __str__(self):
        return "a is " + str(self._a) + ", b is " + str(self._b)


if __name__=="__main__":
    ntfak = NTFAK(5)
    
    print "OPPGAVE 4"

    ntfak.printStatus()
    
    print "OPPGAVE 5"
    ntfak.flyttAlleEiendeler()
    ntfak.printStatus()
    
    
    print "OPPGAVE 7"
    it = Thing()
    print it.foo(2)
    print it.bar(3)
    print it
    
