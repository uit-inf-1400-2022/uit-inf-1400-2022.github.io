# 1a

```python

# Velger å implementere __init__-metoder

class Transportmiddel:
  def __init__(self, lastekapasitet, personkapasitet, vekt):
    self.lastekapasitet = lastekapasitet
    self.personkapasitet = personkapasitet
    self.vekt = vekt

class Personbil(Transportmiddel):
  def __init__(self, lastekapasitet, personkapasitet, vekt, piggdekk):
    super().__init__(lastekapasitet, personkapasitet, vekt)
    self.piggdekk = piggdekk

class Buss(Transportmiddel):
  def __init__(self, lastekapasitet, personkapasitet, vekt, piggdekk, kjetting):
    super().__init__(lastekapasitet, personkapasitet, vekt)
    self.piggdekk = piggdekk
    self.kjetting = kjetting

class Lastebil(Transportmiddel):
  def __init__(self, lastekapasitet, personkapasitet, vekt, piggdekk, kjetting):
    super().__init__(lastekapasitet, personkapasitet, vekt)
    self.piggdekk = piggdekk
    self.kjetting = kjetting

class Tog(Transportmiddel):
  pass
```

# 1b

```python

# Da init-metoden er definert i 1a, viser jeg bare at jeg lager ett objekt
# Dette objektet har attributter:
# piggdekk, kjetting
# lastekapasitet, personkapasitet, vekt - arvet fra parent

lastebil = Lastebil(1000, 2, 1500, true, false)
```

# 2a

```python

def slitasje(transportmiddel):
  sum = 0
  for t in transportmiddel:
    if isinstance(t, Bil):
      sum += FAKTOR_BIL
    if isinstance(t, Buss):
      sum += FAKTOR_BUSS
    if isinstance(t, Lastebil):
      sum += FAKTOR_LASTEBIL
    if isinstance(t, Tog):
      sum += FAKTOR_TOG
  return sum
```

# 2b

```python
class Lastebil(Transportmiddel):
  SLITASJE_FAKTOR = 300
  def __init__(self, lastekapasitet, personkapasitet, vekt, piggdekk, kjetting):
    super().__init__(lastekapasitet, personkapasitet, vekt)
    self.piggdekk = piggdekk
    self.kjetting = kjetting

def slitasje(transportmiddel):
  return sum((t.SLITASJE_FAKTOR for t in transportmiddel))
```


# 3a

Siden utregningen av slitasje for lastebil og buss er lik, så er det naturlig å generalisere disse ved hjelp av en ny klasse (Tungtransport), hvor slitasje-utregningen er definert.

# 3b

Ved å implementere en slit()-metode i hver klasse som regner ut slitasjen for den klassen av kjøretøy, så vil den totale slitasje-funksjonen kunne kalle på denne metoden, uansett hvilken type kjøretøy som kommer inn.

# 3c

```python

class Transportmiddel:
  def __init__(self, lastekapasitet, personkapasitet, vekt):
    self.lastekapasitet = lastekapasitet
    self.personkapasitet = personkapasitet
    self.vekt = vekt

class Personbil(Transportmiddel):
  SLITASJE_FAKTOR = 10
  def __init__(self, lastekapasitet, personkapasitet, vekt, piggdekk):
    super().__init__(lastekapasitet, personkapasitet, vekt)
    self.piggdekk = piggdekk

  def slit(self):
    slitasje_verdi = self.vekt * self.SLITASJE_FAKTOR
    if self.piggdekk:
      slitasje_verdi *= 3
    return slitasje_verdi

class Tungtransport(Transportmiddel):
  def __init__(self, lastekapasitet, personkapasitet, vekt, piggdekk, kjetting):
    super().__init__(lastekapasitet, personkapasitet, vekt)
    self.piggdekk = piggdekk
    self.kjetting = kjetting

  def slit(self):
    slitasje_verdi = self.vekt * math.log(self.vekt) * self.SLITASJE_FAKTOR
    if self.piggdekk:
      slitasje_verdi *= 3
    if self.kjetting:
      slitasje_verdi *= 10
    return slitasje_verdi

class Buss(Tungtransport):
  SLITASJE_FAKTOR = 100

class Lastebil(Tungtransport):
  SLITASJE_FAKTOR = 300

class Tog(Transportmiddel):
  SLITASJE_FAKTOR = 0

  def slit(self):
    return 0
```

# 4a

1. Vi kan gjøre id-attributten privat, og implementere en setter-metode som brukes for å sette id-en, som sikrer at id ikke blir satt til ett negativt tall.

2. Vi kan ha en property-metode som sikrer at id ikke blir satt til ett negativt tall.

# 4b

1. Vi kan raise en exception hvis den blir forsøkt satt til noe negativt.

2. Vi kan bruke absoluttverdien av tallet som blir sendt inn.

# 4c

```python
# Implementerer tilnærming 2 fra a, og tilnærming 1 fra b

class Document:
  def __init__(self):
    self._id = 0
    self.name = ""
    self.contents = []

  def get_info(self):
    return (self.id, self.name, self.contents)

  @property
  def id(self):
    return self._id

  @id.setter
  def id(self, value):
    if value < 0:
      raise ValueError("Attempted to set document ID to negative value")
    self._id = value
```

Kunden trenger ikke endre sin kode.

# 5a

Klasse vs. objekt:

En klasse er en definisjon av en type - den beskriver hvilke variabler, konstanter, og metoder som alle objekter av denne typen inneholder. Ett objekt er en realisering av en type, hvor variablene får verdier.

Multiple inheritance:

Multiple inheritance betyr at en klasse arver fra flere foreldre-klasser, selv om foreldre-klassene ikke har noe med hverandre å gjøre. Dette fører til at child-klassen får alle unike metoder, variabler, og konstanter fra begge foreldreklassen. Ved konflikter mellom metoder vil bare en av parent-metodene bli aksesserbar av child-klassen.
