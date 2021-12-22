# -*- coding: utf-8 -*-
import random


byer = ["London", "Tromso", "Oslo", "Berlin", "Moskva"]

class FlyttetTing(object):
    def __init__(self):
        self.siste_posisjon = None
        self.neste_posisjon = random.choice(byer)
        self.ankomst_tid = random.randint(0,1000)

    
class FlyttetBy(FlyttetTing):
    def __init__(self):
        FlyttetTing.__init__(self)
        self.navn = random.choice(byer)

    def __repr__(self):
        return self.navn+" "+str(self.ankomst_tid)
    
class FlyttetBat(FlyttetTing):
    def __init__(self):
        FlyttetTing.__init__(self)
        
class FlyttetFly(FlyttetTing):
    def __init__(self):
        FlyttetTing.__init__(self)

class RomskipPassering():
    def __init__(self):
        self.register_nummer = None
        self.posisjon = None
        self.tid = random.randint(1, 1000)
        self.flyttede_ting = [FlyttetBy() for x in range(4)]
    
    def __repr__(self):
        return self.__class__.__name__+" "+str(self.tid)
    
class PasseringsRegister():
    def __init__(self):
        self.passeringer = sorted([RomskipPassering() for x in range(5)], key=lambda passering: passering.tid, reverse=True)
        #print self.passeringer
        
    def finnBy(self, navn):
        #denne linjen henter ut alle passeringer som innvolverer en by med et gitt navn. Alternativ til forslaget under, og for å vise hvordan man kan få en dobbel løkke i en setning
        #by_passeringer = [(by, passering) for passering in self.passeringer for by in passering.flyttede_ting if isinstance(by, FlyttetBy) and by.navn==navn]

        #print by_passeringer
        
        
        
        #fungerer siden self.passeringer er sortert nyest til eldst, stopper ved første treff for en by
        for passering in self.passeringer:
            for ting in passering.flyttede_ting:
                if isinstance(ting, FlyttetBy) and ting.navn == navn:
                    return [ting.navn, ting.siste_posisjon, ting.neste_posisjon, ting.ankomst_tid]
        return None

    #lager en dictionary med destinasjoner som nøkkel, og listen av alle som har reist til den destinasjonen, med tidspunkt, som verdi.
    def skrivutAnkomster(self):
        destinasjoner = {}
        for passering in self.passeringer:
            for ting in passering.flyttede_ting:
                if isinstance(ting, FlyttetBy):
                    if destinasjoner.has_key(ting.neste_posisjon) == False:
                        destinasjoner[ting.neste_posisjon] = [(ting.navn, ting.ankomst_tid)]
                    else:
                        destinasjoner[ting.neste_posisjon].append((ting.navn, ting.ankomst_tid))
        return destinasjoner
    
if __name__ == "__main__":
    register = PasseringsRegister()
    print register.finnBy("Oslo")
    print register.skrivutAnkomster()
