# Modulin avulla luodaan, luetaan ja kirjoitetaan CSV-tiedostoja

# Kirjastojen ja modulien lataukset
import csv

# Luodaan otsikot CSV-tiedostoon
def luo_otsikot(tiedosto):
    """Luodaan CSV-tiedostoon tarvittavat sarakeotsikot

    Args:
        tiedosto (string): muokattavan tiedoston nimi
    """

# Määritellään csv-tiedosto, erotin ja tekstitunniste    
    with open(tiedosto, 'w') as datatiedosto:
        csv_kirjoittaja = csv.writer(datatiedosto, delimiter = ';', quotechar = '"')
        csv_kirjoittaja.writerow(['Etunimi', 'Sukunimi', 'Pituus', 'Paino', 'Ikä', 'Sukupuoli', 'Tavoitepaino'])

# Lisätään rivejä CSV-tiedostoon
def lisaa_tiedot(tiedosto, etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino):
    """Lisää CSV-tiedostoon uuden datarivin

    Args:
        tiedosto (string): CSV-tiedoston nimi
        etunimi (string): Etunimi
        sukunimi (string): Sukunimi
        pituus (string): Pituus (cm)
        paino (string): Paino (kg)
        ika (string): Ikä (v)
        sukupuoli (string): Mies 1, nainen 0
        tavoitepaino (string): Tavoitepaino (kg)
    """
    with open(tiedosto, 'a') as datatiedosto:
        csv_kirjoittaja = csv.writer(datatiedosto, delimiter = ';', quotechar = '"')
        csv_kirjoittaja.writerow([etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino])

# Luetaan tiedot luetteloon ja palautetaan luettelo
def lue_rivit(tiedosto):
    """Palauttaa CSV-tiedoston sisällön listana

    Args:
        tiedosto (string): Palautettavan CSV-tiedoston nimi

    Returns:
        list: Lista otsikoista ja arvoista
    """
    
    with open(tiedosto, 'r') as datatiedosto:
        csv_lukija = csv.reader(datatiedosto, delimiter = ";", quotechar = '"')
        for rivi in csv_lukija:
            print(rivi)
        # return csv_lukija



if __name__ == "__main__":

    """     # Lisätään testimielessä rivejä
    lisaa_tiedot('bmidata.csv', 'Mika', 'Vainio', '171', '72', '59','1', '70')
    lisaa_tiedot('bmidata.csv', 'Mikko', 'Viljanen', '176', '80', '50','1', '75') """

    # Luetaan tiedot
    with open('bmidata.csv', 'r') as testiluku:
        print(testiluku.read())

    # Luetaan tiedot listaan ja käydään se riveittäin läpi
    tulokset = lue_rivit('bmidata.csv')
    for tulos in tulokset:
        print(tulos)