from src import blockpi

def test_get_empty_screen():
    game = blockpi.BlockPi()
    screen = game.get_screen()

    empty = [0, 0, 0]
    empty_screen = [empty] * 64

    assert screen == empty_screen

