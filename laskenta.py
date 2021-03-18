# Modulin funktioilla voidaan laskea painoindeksi (BMI) ja kehon rasvaprosentti

# Funktioiden määrittelyt

# Painoindeksi
def bmi(paino, pituus):
    """Laskee painoindeksin kaavalla paino jaettuna pituuden neliöllä

    Args:
        paino (float):paino kiloina (kg)
        pituus (float): pituus senttimetreinä (cm)

    Returns:
        float: painoindeksi
    """
    painoindeksi = paino / (pituus/100) ** 2
    return painoindeksi
    
# Aikuisen rasvaprosentti
def rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee aikuisen henkilön kehon rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): ikä vuosina
        sukupuoli (int): 1 - Miehet, 0 - Naiset

    Returns:
        float: kehon rasvaprosentti
    """
    rprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    return rprosentti

# Lapsen rasvaprosentti
def lapsen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee lapsen kehon rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): ikä vuosina
        sukupuoli (int): 1 - Miehet, 0 - Naiset

    Returns:
        float: kehon rasvaprosentti
    """
    lapsen_rprosentti = 1.51 * bmi - 0.7 * ika - 3.6 * sukupuoli + 1.4
    return lapsen_rprosentti

# Testit
if __name__ == '__main__':
    
    # 1. testi oma painoindeksi
    pituus = 171
    paino = 74.9
    omabmi = bmi(paino, pituus)
    print('Pituus:', pituus, 'Paino:', paino, 'Painoindeksi', omabmi) 

    # 2. testi oma rasvaprosentti
    ika = 9
    sukupuoli = 1
    print('Rasvaprosentti:', lapsen_rasvaprosentti(omabmi, ika, sukupuoli))