#Høst 2010
#Oppgave 4 

class PasseringsRegister:
    def __init__(self):
        self.passeringer = []
        
    def finnBy(self,bynavn):
        i = 1
        while len(self.passeringer) - i >= 0:
            passering = self.passeringer[-i]
            for object in passering.movedObjects
                if isinstance(object,FlyttetBy):
                    if object.name  == byNavn:
                        return[object.name,object.lastPast,object.expectedPas,object.expetedTime]
            i++
        return


#oppgave 5

def skriv_ut_anhouster(self):
    result = {}
    
    for passering in self.passeringer:
        for object in passering.moved.Objects:
            if isintance(object,FlyttetBy)
                if object.expectedDestination in result.keys():
                    result[Object.expectedDestination].append((obj.name,obj.time_arrive))
                else:
                    result[Object.expectedDest] = []
                    result[Object.expectedDest].append((object.name,object.time_arrive))
    
    return result   
                    
