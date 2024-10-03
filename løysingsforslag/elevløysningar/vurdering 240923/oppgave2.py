import random

# Datasett laget med chatgpt (i etterkant av prøven)
datasett = {
    "Norge": {
        "Hovedstad": "Oslo",
        "Naboland": ["Sverige", "Finland", "Russland"],
        "Innbyggertall": 5_425_270  # Estimert innbyggertall for 2023
    },
    "Sverige": {
        "Hovedstad": "Stockholm",
        "Naboland": ["Norge", "Finland"],
        "Innbyggertall": 10_521_556  # Estimert innbyggertall for 2023
    },
    "Danmark": {
        "Hovedstad": "København",
        "Naboland": ["Tyskland"],
        "Innbyggertall": 5_932_654  # Estimert innbyggertall for 2023
    },
    "Finland": {
        "Hovedstad": "Helsinki",
        "Naboland": ["Sverige", "Norge", "Russland"],
        "Innbyggertall": 5_565_718  # Estimert innbyggertall for 2023
    },
    "Kina": {
        "Hovedstad": "Beijing",
        "Naboland": ["Afghanistan", "Bhutan", "India", "Kazakhstan", "Kirgizistan", "Laos", "Mongolia", "Myanmar", "Nepal", "Nord-Korea", "Pakistan", "Russland", "Tadsjikistan", "Vietnam"],
        "Innbyggertall": 1_411_778_724  # Estimert innbyggertall for 2023
    },
    "Russland": {
        "Hovedstad": "Moskva",
        "Naboland": ["Norge", "Finland", "Estland", "Latvia", "Litauen", "Polen", "Belarus", "Ukraina", "Georgia", "Aserbajdsjan", "Kasakhstan", "Kina", "Mongolia", "Nord-Korea"],
        "Innbyggertall": 146_170_015  # Estimert innbyggertall for 2023
    },
    "Japan": {
        "Hovedstad": "Tokyo",
        "Naboland": ["USA"],  # Japan har ingen landgrenser
        "Innbyggertall": 125_584_838  # Estimert innbyggertall for 2023
    },
    "Tyskland": {
        "Hovedstad": "Berlin",
        "Naboland": ["Danmark", "Polen", "Tsjekkia", "Østerrike", "Sveits", "Frankrike", "Luxembourg", "Belgia", "Nederland"],
        "Innbyggertall": 83_294_633  # Estimert innbyggertall for 2023
    },
    "USA": {
        "Hovedstad": "Washington D.C.",
        "Naboland": ["Canada", "Mexico"],
        "Innbyggertall": 334_805_269  # Estimert innbyggertall for 2023
    },
    "India": {
        "Hovedstad": "New Delhi",
        "Naboland": ["Pakistan", "Kina", "Nepal", "Bhutan", "Bangladesh", "Myanmar"],
        "Innbyggertall": 1_408_618_000  # Estimert innbyggertall for 2023
    }
}

# globale variabler
brukte_spørsmål = []
resultater = []
poeng = 0

def Get_Input(input_streng: str, input_type: int):
    """Henter input og sørger for at det er gyldig med hensyn på input type."""
    inp = input(input_streng + "\n")

    # Sørger for at bruker ikke kan sende inn blankt svar med et uhell
    if inp == "":
        print("Du sendte inn et tomt svar")
        return Get_Input(input_streng, input_type)

    # Håndterer input slik de ulike input typene krever
    match input_type:
        case 0:
            # Input er en streng
            return inp.lower()
        case 1:
            # Input skal være flere land, så dette splittes til en liste
            return inp.lower().split()
        case 2:
            # Sørger for at input er et heltall
            try:
                return int(inp.strip())
            except:
                print("Input må være et tall!")
                return Get_Input(input_streng, input_type)
                


def Quiz_runde():
    """
    Spiller en runde av quizen. Skaffer input, lager spørsmål, regner poeng 
    """
    # Velger et tilfeldig land og kategori
    land = random.choice(list(datasett.keys()))
    kategori = random.choice(list(datasett[land].keys()))

    # Sørger for at landet og kategorien ikke er brukt
    while [land, kategori] in brukte_spørsmål:
        land = random.choice(list(datasett.keys()))
        kategori = random.choice(list(datasett[land].keys()))

    # Legger til spørsmålet i brukte_spørsmål for å unngå gjenbrukte spørsmål
    brukte_spørsmål.append([land, kategori])    

    # Skaffer input basert på kategori
    inp = ""
    match kategori:
        case "Hovedstad":
            inp = Get_Input(f"Hva er hovedstaden i {land}?", 0)
        case "Naboland":
            inp = Get_Input(f"Hvilke naboland har {land}?", 1)

            # Kategorien "naboland" har en annerledes poengregning og måte å gi tilbakemelding på. Av den grunn har denne en egen kodeblokk for å håndtere dette.
            
            # Teller antall riktige svar, trekke ifra om man har svart feil. 
            riktige = 0
            for g in inp:
                if g in list(map(lambda x: x.lower(),datasett[land][kategori])):
                    riktige += 1
                else:
                    riktige -= 1
            p = riktige/len(datasett[land][kategori]) # Beregner poeng basert på hvor mange av de mulige riktige svarene man svarte
            if p < 0: p = 0 # Sørger for at man ikke blir trukket i poeng

            if p == 1:
                print(f"Du fikk alle landene rett! Du har nå {poeng + 1} poeng!")
                return 1
            elif p == 0:
                print(f"Dette fikk du ikke helt til... Nabolandene til {land} er {", ".join(datasett[land][kategori])}. Du har {poeng} poeng.")
                return 0
            print(f"Dette fikk du delvis til. Nabolandene til {land} er {", ".join(datasett[land][kategori])}. Du har nå {poeng + p} poeng!")
            return round(p, 2)
                
        case "Innbyggertall":
            inp = Get_Input(f"Hvor mange innbyggere er det i {land}?", 2)

    # Poeng og tilbakemelding for kategoriene "hovedstad" og "innbyggertall"
    if inp == datasett[land][kategori]:
        print(f"Riktig! Du har nå {poeng + 1} poeng!")
        return 1
    print(f"Galt svar! Riktig svar er {datasett[land][kategori]}. Du har {poeng} poeng.")
    return 0

# Hovedløkken for spillet. Går gjennom 3 runder.
print("Klar for quiz?")
for i in range(1,4):
    print(f"\n\nRunde {i}:")
    # Kjører Quiz_runde funksjonen og lagrer poengene fra runden i runde.
    runde = Quiz_runde()
    if runde: # Hvis man ikke fikk 0 poeng
        poeng += runde # Legger til i poengsummen

        resultater.append(True) # Lagrer resultatet fra spørsmålet
    else:
        resultater.append(False) # Lagrer resultatet fra spørsmålet


# Oppsummeringen hvor spørsmålene blir repetert med fasit, og om du svarte galt eller riktig på dette spørsmålet.
print(f"\n\nDa var quizen over! Du fikk {poeng} ut av 3 poeng!\nHer er en liten oppsummering av spørsmålene:")
i = 1
for spørsmål in brukte_spørsmål:
    if spørsmål[1] == "Naboland": # "naboland" måtte skrives på en annen måte
        print(f"\n{i}. {spørsmål[0]}s {spørsmål[1].lower()} er {", ".join(datasett[spørsmål[0]][spørsmål[1]])}")
    else:
        print(f"\n{i}. {spørsmål[0]}s {spørsmål[1].lower()} er {datasett[spørsmål[0]][spørsmål[1]]}")
    
    
    if resultater[i-1]:
        print("  -Dette spørsmålet svarte du riktig på!")
    else:
        print("  -Dette spørsmålet svarte du feil på.")
    i+=1

