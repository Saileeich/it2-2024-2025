import random


def Tilfeldige_Tegn(streng: str) -> str:
    """Konverterer en streng til en streng av samme lengde hvor bokstaver er byttet ut med tilfeldige symboler"""
    SYMBOLER = ["@", "#", "£", "$", "%", "&", "?", "§", "!", "*", "+", "-"]
    _res = ""
    for b in streng:
        if b != " ":
            _res += random.choice(SYMBOLER)
        else:
            _res += b
    return _res


def Erstatningsord(streng: str) -> str:
    """Erstatter ord fra en dict for å sensorerer med finere ord"""
    ERSTATNINGSORD = {
        "fis": "promp",
        "skibidi": "spinnvill",
        "sigma": "person med høyere autoritet",
        "gyatt": "bakdel",
    }

    if (x := Prosesser_Ord(streng).lower()) in ERSTATNINGSORD.keys():
        return ERSTATNINGSORD[x]


def Prosesser_Ord(streng: str) -> str:
    """Prosesserer en streng slik at den er klar for å gå gjennom sensur-sjekken"""
    SYMBOLER = ["@", "#", "£", "$", "%", "&", "?", "§", "!", "*", "+", "-"]
    if streng == "FIS":
        return streng
    _res = ""
    for l in streng.lower():
        if l in SYMBOLER:
            continue
        _res += l
    return _res


def Sensurering(*args: str) -> list:
    """Tar in strenger og filtrerer vekk 'stygge' ord. Returnerer en liste med korrigerte strenger"""
    BLACKLIST = ["fis", "skibidi", "sigma", "gyatt"]
    _res = []
    for arg in args:
        _wrk = []
        for ord in arg.split(" "):
            if Prosesser_Ord(ord) in BLACKLIST:
                _wrk.append(
                    Erstatningsord(ord)
                )  # Benytt enten Erstatningsord() eller Tilfeldige_tegn() for å sensurere
            else:
                _wrk.append(ord)
        _res.append(" ".join(_wrk))
    return _res


print(
    Sensurering(
        "Fis fra g+y#a!t!t til en Skibidi SigMa med fiskale meninger om skiorganisasjonen FIS"
    )
)
