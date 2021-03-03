# Moduli syötteen oikeellisuuden (sanity) tarkistamiseen
"""Tarkistaa käyttäjän syötteen oikeellisuuden tarkistusfunktioiden avulla
"""


# Funktioiden määrittelyt
def on_jarkeva(syote, alaraja, ylaraja):
    """
    Puhdistaa merkkijonosta ylimääräiset tulostumattomat merkit ja välilyönnit
    sekä selvittää onko syötetty arvo annettujen rajojen sisällä. 
    Funktio muutta desimaali pilkun desimaalipisteeksi.


    Args:
        syote (string): Näppäimistöltä syötetty arvo
        alarja (float): pienin sallittu arvo
        ylaraja (float): suurin sallittu arvo

    Returns (float) : Käyttäjän syöttämä arvo numeerisena
    """

    # Poistetaan whitespace merkit merkkijonon alusta
    puhdistettu_syote = syote.lstrip()

    #  Poistetaan whitespace merkit merkkijonon alusta
    puhdistettu_syote = puhdistettu_syote.rstrip()

    # Selvitetään onko merkkijonossa pilkku (,)
    pilkunpaikka = puhdistettu_syote.find(',')

    # Jos pilkku löytyy, korvataan pisteellä
    if pilkunpaikka != -1:
        korjattu_syote = puhdistettu_syote.replace(',', '.')
    else:
      korjattu_syote = puhdistettu_syote

    # Muutetaan korjattu syöte merkkijonosta liukuluvuksi
    try:
        luku = float(korjattu_syote)
    except:
        print('Syötetyssä tiedossa on ylimääräisiä merkkejä, vain numerot sallittu')
        luku = 0
    # Tarkistetaan, ettei syöte ole alarajan alapuolella
    try:
        if luku < alaraja:
            raise Exception('Syöttämäsi arvo on alle sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Tarkistetaan, ettei syöte ole ylärajan yläpuolella
    try:
        if luku > ylaraja:
            raise Exception('Syöttämäsi arvo on yli sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)
    
    # Palautetaan luku
    return luku

def liukuluku_ok(syote, alaraja, ylaraja):
    """Tarkistaa syötteen olevan numeerinen ja muuttaa sen liukuluvuksi. Syötteellä on alaraja ja yläraja
    
    Args:
        syote (string): Syötteenä saatu arvo
        alaraja (float): pienin hyväksyttävä arvo
        ylaraja (float): suurin hyväksyttävä arvo

    Returns:
        list: Palauttaa arvon (float), virhekoodin (int), virhesanoman (string)
    """
    # Puhdistetaan syötteestä ylimääriset merkit (white space)
    puhdistettumerkkijono = syote.strip()

    # Tutkitaan onko syötteessä pilkku ja etsitään sen paikka
    pilkunpaikka = puhdistettumerkkijono.find(',')

    # Jos pilkku löytyi, korvataan pisteellä
    if pilkunpaikka != -1: # Jos ei löydy indeksi on aina -1
        numeroarvo = puhdistettumerkkijono.replace(',', '.') # Muutetaan
    else:
        numeroarvo = puhdistettumerkkijono # ei muuteta

    # Etsitään desimaalipistettä merkkijonosta
    pisteenpaikka = numeroarvo.find('.')

    # Jos desimaalipiste löytyy, jaetaan pisteen kohdalta erillisiksi merkkijoiksi
    if pisteenpaikka != -1:
        osat = numeroarvo.split('.') # Syntyy lista osista
        osien_maara = len(osat)
        if osien_maara > 2:
            virhekoodi = 1
            virhesanoma = "Syötteessä on useita desimaalipisteitä tai useita arvoja: vain yksi liukuluku on sallittu"
            arvo = 0
        #TODO: tee osien numeerisuus testi valmiiksi
        # elif condition:
            
    tulokset = None
    return tulokset
    
# Jos sanity.py-tiedostoa ajetaan terminaalissa, suoritetaan testit
if __name__ == '__main__':
    
    # Testataan toimintaa
    tulos = on_jarkeva('sata', 1, 500)
    print(tulos)
syote = ' 10.5   '
print(syote.strip(), 'kiloa')