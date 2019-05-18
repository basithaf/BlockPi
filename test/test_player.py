from src import player

def test_get_location():
    p = player.Player()
    assert p.get_location() == (0, 0)