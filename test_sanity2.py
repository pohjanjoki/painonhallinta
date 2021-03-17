# Sanity2-modulin testit

# Modulin lataus
import sanity2

# Arvo rajojen sisällä, virhekoodi 0, virhesanoma Arvo OK
def test_rajatarkistus():
    assert sanity2.rajatarkistus(100, 20, 300) == [0, 'Arvo OK'] 
