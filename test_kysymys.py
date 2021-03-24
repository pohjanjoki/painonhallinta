# Kysymysmodulin testit

# Modulien ja kirjatojen lataukset
import kysymys

# TODO: tee testit ja kirjoita Wikiin ohjeet syötteen automatisoinnista

# Syöte ok
def test_kysymys_ok():
    kysymys.input = lambda: '50'
    assert kysymys.kysy_liukuluku('Painosi (kg)', 20, 350) == 50
# Syötteessä tietotyyppivirhe

# Alle alarajan

# Yli ylärajan