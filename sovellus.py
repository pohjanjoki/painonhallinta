# Tämä on painonhallintasovelluksen pääohjelma

# Kirjastojen ja modulien käyttöönotot
import sanity2
import laskenta

# Varsinaisen pääohjelman alku

# Työsilmukka, ikuinen silmukka, jossa on poistumistoiminto (ehto True on aina voimassa)
uusi = 'K'
while True:

    # Kysytään käyttäjältä paino
    tapahtui_virhe = True

    # Silmukka jossa pyöritään kunnes saadaan järkevä arvo
    while tapahtui_virhe == True:
        paino_str = input('Paino (kg)? ')
        tulokset = sanity2.liukuluvuksi(paino_str)

        # Katsotaan onko virhekoodi 0, ja tallennetaan arvo muuttujaan paino
        if tulokset[0] == 0:

            # TODO: lisää raja-arvotarkistukset
            paino = tulokset[2]
            tapahtui_virhe = False

        # Jos virhekoodi ei ole 0, tulostetaan virheilmoitus    
        else:
            print(tulokset[1])

    # Testi
    print('Ja paino oli', paino, 'kg')

    # TODO: Muille tiedoille vastaavat kyselysilmukat
              
    '''
    pituus_str = input('Pituus (m)? ')
    pituus = 

    print('Painoindeksisi on', bmi(paino, pituus))
    '''
    # Poistuminen ikuisesta silmukasta
    uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/E)')
    if uusi == 'E':
        break
        


