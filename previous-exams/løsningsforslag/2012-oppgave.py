#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Det er ikke angitt noe sted at man skal ta med initielle verdier til attributtene i
# __init__, derfor kan vi godt utelate det og anta at det settes på et eller annet vis i
# koden ellers.

class Hendelse(object):
    def __init__(self):
        self.rute = None
        self.tidspunkt = None
    def forsinketLengreEnn(self, minutter):
        # Dette er "optional" siden det ikke er spesifisert i oppgaven, men det er
        # ofte en god idé å kaste en exception hvis det ikke er meningen at noen skal
        # bruke metoden i baseklassen. 
        raise Exception("not allowed on the base class")

class Forsinkelse(Hendelse):
    def __init__(self):
        Hendelse.__init__(self)
        self.minutes = None

    def forsinketLengreEnn(self, minutter):
        return self.minutes > minutter

class Innstilling(Hendelse):
    def __init__(self):
        Hendelse.__init__(self)

    def forsinketLengreEnn(self, minutter):
        return True


class Buss(object):
    def __init__(self):
        self.rute = None
        self.hendelser = []
    def kanBrukeKjetting(self):
        # Annet alternativ til default-metode: returner noe som gir mening for
        # de fleste underklassene.
        return False 

class LangBuss(Buss):
    def __init__(self):
        Buss.__init__(self)
    def kanBrukeKjetting(self):
        return True

class ElBuss(Buss):
    def __init__(self):
        Buss.__init__(self)


class Busspark(object):
    def __init__(self):
        self.busser = []

    def finnHendelser(self, minForsinkelse):
        antFors = 0
        antInst = 0
        forsinkelser = []
        for buss in self.busser:
            for hendelse in buss.hendelser:
                if hendelse.forsinketLengreEnn(minForsinkelse):
                    if isinstance(hendelse, Forsinkelse):
                        antFors += 1
                    elif isinstance(hendelse, Innstilling):
                        antInst += 1
                    forsinkelser.append(hendelse)
        return (antInst, antFors, forsinkelser)
                


