# Sanity2-modulin testit

# Modulin lataus
import sanity2

# Arvo rajojen sisällä, virhekoodi 0, virhesanoma 'Arvo OK'
def test_rajatarkistus_oikein():
    assert sanity2.rajatarkistus(100, 20, 300) == [0, 'Arvo OK'] 

# Arvo alle alarajan, virhekoodi 1, virhesanoma 'Arvo on alle alarajan (20)'
def test_rajatarkistus_alle():
    assert sanity2.rajatarkistus(10, 20, 300) == [1, 'Arvo on alle alarajan (20)'] 

# Arvo yli ylärajan, virhekoodi 2, virhesanoma 'Arvo on yli ylärajan (300)'
def test_rajatarkistus_yli():
    assert sanity2.rajatarkistus(350, 20, 300) == [2, 'Arvo on yli ylärajan (300)']

# LIUKULUKUMUUNNOS TESTIT

# Syötteenä kokonaisluku, virhekoodi 0, virheilmoitus Syöte OK, arvo liukulukuna
def test_liukuluku_kokonaisluku():
    assert sanity2.liukuluvuksi('15') == [0, 'Syöte OK', 15.0]

# Syötteenä liukuluku, jossa desimaalipiste
def test_liukuluku_liukuluku():
    assert sanity2.liukuluvuksi('15.0'): == [0, 'Syöte OK', 15.0]

# Syötteenä liukuluku, jossa desimaalipilkku: automaattinen korjaus
def test_liukuluku_liukuluku():
    assert sanity2.liukuluvuksi('15,0'): == [0, 'Syöte OK', 15.0]

# Syötteenä liukuluku, jossa useampi desimaalipiste: virhe
def test_liukuluku_liukuluku():
    assert sanity2.liukuluvuksi('15.0.7'): == [0, 'Syöte OK', 15.0]

# Syötteenä liukuluku, jossa useampi desimaalipilkku: virhe
def test_liukuluku_liukuluku():
    assert sanity2.liukuluvuksi('15,0,7'): == [0, 'Syöte OK', 15.0]

# Syötteenä mukana kirjaimia
def test_liukuluku_liukuluku():
    assert sanity2.liukuluvuksi('15.0 kg'): == [0, 'Syöte OK', 15.0]



