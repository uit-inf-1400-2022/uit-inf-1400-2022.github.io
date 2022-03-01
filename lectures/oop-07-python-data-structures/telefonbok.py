from dataclasses import dataclass
import string

@dataclass
class Person:
    navn: string
    epost: string
    tlfnr: string

telefonbok = {"Caroline": Person("Caroline", "c@com.com", "46464646")}
telefonbok["Berit"] = Person("Berit", "b@com.com", "22222222")
telefonbok["Arne"] = Person("Arne", "a@com.com", "12345678")

#print(telefonbok["Arne"])


telefonbok2 = {}

telefonbok2["Ali"] = {"e-post": "ali@com.com", "tlf": "54545454"}
telefonbok2["Lars"] = {"e-post": "lars@com.com", "tlf": "33333333"}

for k, v in telefonbok2.items():
    print("Navn:", k, "Data:", v)



