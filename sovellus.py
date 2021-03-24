# Tämä on painonhallintasovelluksen pääohjelma

# Kirjastojen ja modulien käyttöönotot
import laskenta
import kysymys

# Varsinaisen pääohjelman alku

# Työsilmukka, ikuinen silmukka, jossa on poistumistoiminto (ehto True on aina voimassa)
uusi = 'K'
while True:

    # Tehdään kysymykset modulin kysymys.py funktiota käyttämällä
    paino = kysymys.kysy_liukuluku('Paino (kg)', 30, 350)
    pituus = kysymys.kysy_liukuluku('Pituus (cm)', 100, 300)
    ika = kysymys.kysy_liukuluku('Ikä (v)', 3, 125)
    sukupuoli = kysymys.kysy_liukuluku('Sukupuoli nainen: 0, mies:1', 0, 1)
  
    # Lasketaan ja tulostetaan painoindeksi
    bmi = laskenta.bmi(paino, pituus) 
    print('Henkilön painoindeksi on:', round(bmi, 1))

    # Lasketaan ja tulostetaan kehon rasvaprosentti
    rasvaprosentti = laskenta.rasvaprosentti(bmi, ika, sukupuoli)
    print('Laskennallinen kehon rasvaprosentti on:', round(rasvaprosentti, 1))

    # Poistuminen ikuisesta silmukasta
    uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/e)')
    if uusi.upper() == 'E':
        break
        


