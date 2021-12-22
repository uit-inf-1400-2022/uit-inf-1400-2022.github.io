'''
Øvingsoppgave eksamen INF-1400

Oppgaven går i store trekk ut på å omgjøre et ikke-objektorientert program om til et objektorientert program.
Oppgavene under leder deg på veien og gir deg mulighet til å demonstrere deler av prosessen og vise bruk av begrep i praksis.

NB: på en eksamen er det viktig at du svarer på alt! Les spørsmålene nøye og sjekk dem på nytt etter at du har svart for å se at du har fått med deg alt.

Vi har en prototype på en applikasjon som skal simulere slitasje på en vei, delt inn i flere veistrekninger, og gi beskjed om når deler av veien trenger
vedlikehold. Prototypen har kommet et stykke på vei, men vi må forbedre designet og koden for å utvide den videre.

Oppgave 1:
    Lag et klassediagram for de klassene du tenker er naturlige å ta med, inkludert relasjoner mellom klassene. Løsningen skal demonstrere arv og polymorfi.

Oppgave 2:
    Beskriv hvordan slitasje-oppførselen kan implementeres, og grove trekk for hvordan du endrer den eksisterende koden.
    Beskriv antagelsene du gjør. Forklar hvordan arv og polymorfi brukes i løsningen.

Oppgave 3:
    Implementer det du har beskrevet

Oppgave 4:
    Det har kommet en type overflatedekke man kan legge på veistrekninger uansett hva de er laget av, som skal redusere slitasjen.
    Dette dekket reduserer slitasjen avhengig av hvilken type dekk som brukes (slitasjen fra kjettinger reduseres med 60% f.eks.).
    Lag en klasse som kan representere dette dekket.
    a) Hvordan vil du representere denne klassen i hierarkiet?
    b) Hva må legges til eller endres i koden for å implementere klassen?
    c) Implementer klassen.

'''


import random

types = ["lastebil", "buss", "tog", "bil"]
types_vekting = [10, 2, 1, 50]
dekk_verdi = ["piggfritt", "piggdekk", "kjetting"]
dekk_vekting = [5, 5, 1]

strekning_dekke = ["asfalt", "betong", "grus"]
strekning_vekting = [10, 2, 5]


def lag_kjoretoy():
    kjoretoy = {}
    kjoretoy["type"] = random.choices(types, types_vekting)[0]
    kjoretoy["dekk"] = random.choices(dekk_verdi, dekk_vekting)[0]
    return kjoretoy


def slitasje(kjoretoy):
    slitasje = 0
    if kjoretoy["type"] == "bil":
        slitasje = 10
    if kjoretoy["type"] == "buss":
        slitasje = 100
    if kjoretoy["type"] == "lastebil":
        slitasje = 300
    if kjoretoy["type"] == "tog":
        slitasje = 0
    if kjoretoy["dekk"] == "piggdekk":
        slitasje *= 3
    if kjoretoy["dekk"] == "kjetting":
        slitasje *= 10
    return slitasje


def lag_veistrekning(nummer):
    strekning = {}
    strekning["nummer"] = nummer
    strekning["trenger_vedlikehold"] = False
    strekning["dekke"] = random.choices(strekning_dekke, strekning_vekting)[0]
    if strekning["dekke"] == "asfalt":
        strekning["holdbarhet"] = 10000
    if strekning["dekke"] == "betong":
        strekning["holdbarhet"] = 50000
    if strekning["dekke"] == "grus":
        strekning["holdbarhet"] = 3000
    return strekning


def kjor_over(kjoretoy, strekning):
    strekning["holdbarhet"] -= slitasje(kjoretoy)


if __name__ == "__main__":
    kjoretoy = []
    strekninger = []
    for _ in range(1000):
        kjoretoy.append(lag_kjoretoy())
    for n in range(50):
        strekninger.append(lag_veistrekning(n))
    for k in kjoretoy:
        for s in strekninger:
            kjor_over(k, s)
            if s["holdbarhet"] < 1000 and not s["trenger_vedlikehold"]:
                print("Strekning {} må vedlikeholdes!".format(s["nummer"]))
                s["trenger_vedlikehold"] = True
