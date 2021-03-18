# Tämä on painonhallintasovelluksen pääohjelma

# Kirjastojen ja modulien käyttöönotot
import sanity2
import laskenta

# Varsinaisen pääohjelman alku

# Työsilmukka, ikuinen silmukka, jossa on poistumistoiminto (ehto True on aina voimassa)
uusi = 'K'
while True:

    # Silmukka jossa pyöritään kunnes saadaan järkevä paino
    tapahtui_virhe = True
    while tapahtui_virhe == True:
        paino_str = input('Paino (kg)? ')
        tulokset = sanity2.liukuluvuksi(paino_str)

        # Katsotaan onko virhekoodi 0, ja tallennetaan arvo muuttujaan paino
        if tulokset[0] == 0:
            paino = tulokset[2]
            tarkistettu_paino = sanity2.rajatarkistus(paino, 20, 300)
            
            # Katsotaan onko arvo sallittujen rajojen sisällä tutkimalla virhekoodia
            if tarkistettu_paino[0] == 0:
                tapahtui_virhe = False
            else:
                # Tulostetaan virheimoitus 
                print(tarkistettu_paino[1])
                            
        # Jos virhekoodi ei ole 0, tulostetaan virheilmoitus    
        else:
            print(tulokset[1])

                
    # Silmukka jossa pyöritään kunnes saadaan järkevä pituus
    tapahtui_virhe = True
    while tapahtui_virhe == True:
        pituus_str = input('Pituus (cm)? ')
        tulokset = sanity2.liukuluvuksi(pituus_str)

        # Katsotaan onko virhekoodi 0, ja tallennetaan arvo muuttujaan paino
        if tulokset[0] == 0:
            pituus = tulokset[2]
            tarkistettu_pituus = sanity2.rajatarkistus(pituus, 100, 220)
            
            # Katsotaan onko arvo sallittujen rajojen sisällä tutkimalla virhekoodia
            if tarkistettu_pituus[0] == 0:
                tapahtui_virhe = False
            else:
                # Tulostetaan virheimoitus 
                print(tarkistettu_pituus[1])
                            
        # Jos virhekoodi ei ole 0, tulostetaan virheilmoitus    
        else:
            print(tulokset[1])

    
    # Silmukka jossa pyöritään kunnes saadaan järkevä ikä
    tapahtui_virhe = True
    while tapahtui_virhe == True:
        ika_str = input('Ikä (v)? ')
        tulokset = sanity2.liukuluvuksi(ika_str)

        # Katsotaan onko virhekoodi 0, ja tallennetaan arvo muuttujaan paino
        if tulokset[0] == 0:
            ika = tulokset[2]
            tarkistettu_ika = sanity2.rajatarkistus(ika, 3, 120)
            
            # Katsotaan onko arvo sallittujen rajojen sisällä tutkimalla virhekoodia
            if tarkistettu_ika[0] == 0:
                tapahtui_virhe = False
            else:
                # Tulostetaan virheimoitus 
                print(tarkistettu_ika[1])
                            
        # Jos virhekoodi ei ole 0, tulostetaan virheilmoitus    
        else:
            print(tulokset[1])


    # Silmukka jossa pyöritään kunnes saadaan järkevä sukupuoli
    tapahtui_virhe = True
    while tapahtui_virhe == True:
        sukupuoli_str = input('Sukupuoli (nainen = 0, mies = 1)? ')
        tulokset = sanity2.liukuluvuksi(sukupuoli_str)

        # Katsotaan onko virhekoodi 0, ja tallennetaan arvo muuttujaan paino
        if tulokset[0] == 0:
            sukupuoli = tulokset[2]
            tarkistettu_sukupuoli = sanity2.rajatarkistus(sukupuoli, 0, 1)
            
            # Katsotaan onko arvo sallittujen rajojen sisällä tutkimalla virhekoodia
            if tarkistettu_sukupuoli[0] == 0:
                tapahtui_virhe = False
            else:
                # Tulostetaan virheimoitus 
                print(tarkistettu_sukupuoli[1])
                            
        # Jos virhekoodi ei ole 0, tulostetaan virheilmoitus    
        else:
            print(tulokset[1])

    
    # Lasketaan ja tulostetaan painoindeksi
    bmi = laskenta.bmi(paino, pituus)
    print('Henkilön painoindeksi on:', round(bmi, 1))

    # Lasketaan ja tulostetaan rasvaprosentti
    if ika > 18:
        rasvaprosentti = laskenta.rasvaprosentti(bmi, ika, sukupuoli)
        print('Laskennallinen kehon rasvaprosentti on:', round(rasvaprosentti, 1))

    else:
        lapsen_rasvaprosentti = laskenta.lapsen_rasvaprosentti(bmi, ika, sukupuoli)
        print('Laskennallinen kehon rasvaprosentti on:', round(lapsen_rasvaprosentti, 1))

    # Poistuminen ikuisesta silmukasta
    uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/e)')
    if uusi.upper() == 'E':
        break