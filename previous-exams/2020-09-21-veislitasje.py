import random
import pygame

HEIGHT = 800
WIDTH = 800

veitype = [("grusvei", 10000), ("asfalt", 30000), ("betong", 50000)]
biltype = ["personbil", "lastebil", "buss"]
dekktype = [{"navn": "Summertime Funtime", "slitasje":10, "type":"sommerdekk"},
        {"navn": "Winter Grip", "slitasje":30, "type":"piggdekk"},
        {"navn": "Neverslip", "slitasje":50, "type":"kjetting"}]

def regn_slitasje(bil):
    if bil["biltype"] == "personbil":
        slitasje_faktor = 10
    elif bil["biltype"] == "lastebil":
        slitasje_faktor = 30
    elif bil["biltype"] == "buss":
        slitasje_faktor = 20
    else:
        raise ValueError("Ingen gyldig biltype")

    if bil["dekktype"]["type"] == "kjetting":
        slitasje_faktor *= bil["dekktype"]["slitasje"] / 5
    else:
        slitasje_faktor *= bil["dekktype"]["slitasje"] / 10

    return slitasje_faktor

def slit_vei(vei, slitasje):
    vei["slitasje"] += slitasje
    if vei["slitasje"] > vei["max_slitasje"]:
        vei["slitasje"] = vei["max_slitasje"]
    slitasje_prosent = vei["slitasje"] / vei["max_slitasje"]
    rod_farge = int(slitasje_prosent*255)
    gronn_farge = int((1-slitasje_prosent) * 255)
    vei["farge"] = (rod_farge, gronn_farge , 0)

def lag_bil():
    bil = {}
    bil["dekktype"] = random.choice(dekktype)
    bil["biltype"] = random.choice(biltype)
    return bil

def lag_veistrekning():
    veistrekning = {}
    veistrekning["slitasje"] = 0
    veistrekning["type"], veistrekning["max_slitasje"] = random.choice(veitype)
    veistrekning["farge"] = (0,255,0)
    return veistrekning

def simuler_bil(strekninger):
    bil = lag_bil()
    for strekning in strekninger:
        slit_vei(strekning, regn_slitasje(bil))

def visualiser_strekninger(strekninger, vindu):
    for i, strekning in enumerate(strekninger):
        hoyde = max(min(HEIGHT * (strekning["slitasje"] / strekning["max_slitasje"]), HEIGHT), 10)
        x = i * (WIDTH / len(strekninger))
        vindu.fill(strekning["farge"], pygame.Rect(x, HEIGHT-hoyde, 10, hoyde))

if __name__ == "__main__":
    pygame.init()
    vindu = pygame.display.set_mode((WIDTH,HEIGHT))
    veistrekninger = []
    for i in range(10):
        veistrekninger.append(lag_veistrekning())

    c = pygame.time.Clock()
    while True:
        simuler_bil(veistrekninger)
        vindu.fill((0,0,0))
        visualiser_strekninger(veistrekninger, vindu)
        pygame.display.update()
        c.tick(10)


