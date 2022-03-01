from dataclasses import dataclass
import string

@dataclass
class Hund:
    navn: string
    alder: int
    rase: string

felix = Hund("Felix", 4, "golden")
rudolf = Hund("Rudolf", 10, "norsk reinshund")

print(felix)
felix.alder += 1
print(felix)